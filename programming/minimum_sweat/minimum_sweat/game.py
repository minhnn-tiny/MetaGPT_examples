from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # TODO: Save the user to the database

    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = # TODO: Get the user from the database

    if not user or not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'success': False}), 401

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
