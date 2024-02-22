## views.py
from flask import Flask, request, jsonify, render_template
from services import UserService, AdaptiveLearning
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def response(data=None, error=None, status=200):
    """Utility function for formatting JSON responses."""
    if error:
        return jsonify({'error': error}), status
    return jsonify(data), status

def validate_score(score):
    """Validate that score is a positive integer."""
    try:
        score = int(score)
        if score <= 0:
            raise ValueError
        return True
    except ValueError:
        return False

def validate_login(username, password):
    """Validate login credentials."""
    if len(username) < 3 or len(password) < 6:
        return False
    return True

@app.route('/')
def index():
    """Render the main HTML template for the React frontend."""
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    if not username or not password or not validate_login(username, password):
        return response(error='Invalid login credentials', status=400)
    user_service = UserService()
    user = user_service.login(username, password)
    if user:
        return response(data=user.to_dict())
    else:
        return response(error='Invalid username or password', status=401)

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    data = request.get_json()
    username = data.get('username', '')
    if not username:
        return response(error='Username is required', status=400)
    user_service = UserService()
    result = user_service.logout(username)
    if result:
        return response(data={'message': 'Successfully logged out'})
    else:
        return response(error='Logout failed', status=400)

@app.route('/progress', methods=['GET'])
def get_progress():
    """Get user progress."""
    username = request.args.get('username', '')
    if not username:
        return response(error='Username is required', status=400)
    user_service = UserService()
    progress = user_service.get_progress(username)
    if progress:
        return response(data=progress.to_dict())
    else:
        return response(error='Progress not found', status=404)

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    """Get flashcards based on user's current level."""
    username = request.args.get('username', '')
    if not username:
        return response(error='Username is required', status=400)
    user_service = UserService()
    flashcards = user_service.get_flashcards(username)
    return response(data=[flashcard.to_dict() for flashcard in flashcards])

@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    """Get quizzes based on user's current level."""
    username = request.args.get('username', '')
    if not username:
        return response(error='Username is required', status=400)
    user_service = UserService()
    quizzes = user_service.get_quizzes(username)
    return response(data=[quiz.to_dict() for quiz in quizzes])

@app.route('/update_score', methods=['POST'])
def update_score():
    """Update user score after completing a quiz or flashcard."""
    data = request.get_json()
    username = data.get('username', '')
    score = data.get('score', 0)
    if not username or not validate_score(score):
        return response(error='Username and a positive score are required', status=400)
    user_service = UserService()
    result = user_service.update_score(username, score)
    if result:
        return response(data={'message': 'Score updated successfully'})
    else:
        return response(error='Failed to update score', status=400)

if __name__ == '__main__':
    app.run(debug=True)
