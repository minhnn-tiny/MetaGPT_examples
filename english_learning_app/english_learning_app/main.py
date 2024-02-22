## main.py
from flask import Flask
import app

# Initialize Flask app
def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('config.Config')
    app.init_app(flask_app)
    return flask_app

if __name__ == '__main__':
    my_app = create_app()
    # Fetch the debug mode from the configuration file
    my_app.run(debug=my_app.config.get("DEBUG", False))
