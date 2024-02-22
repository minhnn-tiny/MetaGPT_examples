## config.py

# Importing os module to fetch environment variables if needed
import os

class Config:
    """
    Configuration class to hold all the settings for the Flask application,
    database, and other services. This approach allows for easy adjustments
    and scalability of the application settings.
    """
    
    # Flask application configurations
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_very_secret_key')
    FLASK_APP = os.environ.get('FLASK_APP', 'app.py')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    
    # Database configurations
    # Defaulting to SQLite for simplicity and ease of setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Other service configurations can be added here
    # For example, configurations for logging, email services, etc.
    
    # Adding configurations for the spaced repetition algorithm
    # These values can be adjusted based on the application's needs and testing
    SR_ALGORITHM_INITIAL_INTERVAL = 1  # Initial interval in days for the first repetition
    SR_ALGORITHM_MULTIPLIER = 2  # Multiplier for increasing the interval after each successful repetition
    
    # Configurations for Chart.js
    CHART_JS_VERSION = '2.9.4'

# Example on how to use Config class in other parts of the application:
# from config import Config
# app.config['SECRET_KEY'] = Config.SECRET_KEY
