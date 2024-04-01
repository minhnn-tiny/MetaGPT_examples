from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from utils import generate_token, verify_token
import game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
bcrypt = Bcrypt(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = game.User(data['username'], hashed_password)
    game.db.session.add(new_user)
    game.db.session.commit()
    return jsonify({'message': 'Registered successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = game.User.query.filter_by(username=data['username']).first()
    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    token = generate_token(user.id)
    return jsonify({'token': token})

@app.route('/api/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split(' ')[1]
    user_id = verify_token(token)
    if not user_id:
        return jsonify({'message': 'Invalid token'}), 401
    user = game.User.query.get(user_id)
    return jsonify({'message': f'Welcome {user.username}'})

if __name__ == '__main__':
    game.init_db()
    app.run(debug=True)
