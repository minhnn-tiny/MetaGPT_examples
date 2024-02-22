## app.py
from flask import Flask, jsonify, request, session, redirect, url_for
from models import User, Flashcard, Quiz, Progress
from services import AdaptiveLearning
from database import init_db
import config
from functools import wraps

app = Flask(__name__)
app.config.from_object(config)

# Schema validation imports
from flask_expects_json import expects_json

# Schemas for JSON validation
login_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 1},
        'password': {'type': 'string', 'minLength': 1},
    },
    'required': ['username', 'password']
}

# Authentication decorator to ensure user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Route for user login
@app.route('/login', methods=['POST'])
@expects_json(login_schema)
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    try:
        user = User.login(username, password)
        if user:
            session['user_id'] = user.id  # Assuming User model has an id attribute
            return jsonify({'message': 'Login successful', 'user': user.username}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'message': 'Login failed due to an error'}), 500

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Route to get flashcards based on difficulty level
@app.route('/flashcards/<difficulty_level>', methods=['GET'])
@login_required
def get_flashcards(difficulty_level):
    try:
        flashcards = Flashcard.get_flashcards(difficulty_level)
        return jsonify({'flashcards': flashcards}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route to get quizzes based on difficulty level
@app.route('/quizzes/<difficulty_level>', methods=['GET'])
@login_required
def get_quizzes(difficulty_level):
    try:
        quizzes = Quiz.get_quizzes(difficulty_level)
        return jsonify({'quizzes': quizzes}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route to update user score and get updated level
@app.route('/progress', methods=['POST'])
@login_required
def update_score():
    data = request.get_json()
    score = data.get('score')
    user_id = session['user_id']  # Use session user_id for authentication
    try:
        progress = Progress.update_score(user_id, score)
        return jsonify({'message': 'Score updated', 'level': progress.get_level()}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route to adjust learning path based on user progress
@app.route('/adaptive_learning/<user_id>', methods=['GET'])
@login_required
def adjust_learning_path(user_id):
    try:
        user_progress = Progress.get_progress(user_id)
        adjusted_path = AdaptiveLearning.adjust_learning_path(user_progress)
        return jsonify({'adjusted_path': adjusted_path}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.secret_key = config.SECRET_KEY
    init_db(app.config['DATABASE_URI'])
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
