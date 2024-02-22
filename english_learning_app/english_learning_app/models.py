## models.py
import sqlite3
from typing import List
from contextlib import closing
from werkzeug.security import generate_password_hash, check_password_hash

# Improved database connection function
def get_db_connection():
    return closing(sqlite3.connect('database.db'))

class User:
    def __init__(self, id: int, username: str, password_hash: str, progress: 'Progress'):
        self._id = id
        self._username = username
        self._password_hash = password_hash
        self._progress = progress

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def progress(self):
        return self._progress

    def login(self, username: str, password: str) -> bool:
        with get_db_connection() as conn:
            user = conn.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
        if user and check_password_hash(user['password_hash'], password):
            return True
        return False

    def logout(self) -> None:
        # Implement logout logic as required by the application's architecture
        pass

class Flashcard:
    def __init__(self, id: int, content: str, difficulty_level: str):
        self._id = id
        self._content = content
        self._difficulty_level = difficulty_level

    @property
    def id(self):
        return self._id

    @property
    def content(self):
        return self._content

    @property
    def difficulty_level(self):
        return self._difficulty_level

class Quiz:
    def __init__(self, id: int, questions: List[Flashcard], difficulty_level: str):
        self._id = id
        self._questions = questions
        self._difficulty_level = difficulty_level

    @property
    def id(self):
        return self._id

    @property
    def questions(self):
        return self._questions

    @property
    def difficulty_level(self):
        return self._difficulty_level

class Progress:
    def __init__(self, user_id: int, score: int, level: str):
        self._user_id = user_id
        self._score = score
        self._level = level

    @property
    def user_id(self):
        return self._user_id

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self.update_score_in_db()

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self.update_level_in_db()

    def update_score_in_db(self):
        with get_db_connection() as conn:
            conn.execute('UPDATE progress SET score = ? WHERE user_id = ?', (self._score, self._user_id))
            conn.commit()

    def update_level_in_db(self):
        with get_db_connection() as conn:
            conn.execute('UPDATE progress SET level = ? WHERE user_id = ?', (self._level, self._user_id))
            conn.commit()

class AdaptiveLearning:
    def adjust_learning_path(self, user_progress: Progress) -> None:
        # Enhanced logic for adjusting the learning path based on user progress
        if user_progress.score < 50:
            user_progress.level = 'Beginner'
        elif user_progress.score < 100:
            user_progress.level = 'Intermediate'
        else:
            user_progress.level = 'Advanced'
        # Additional logic to adjust based on more detailed analysis could be added here
