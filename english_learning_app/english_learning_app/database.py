## database.py
import sqlite3
from typing import List, Dict, Any
from contextlib import contextmanager
import os
import logging

# Import configurations
from config import DATABASE_PATH

# Ensure the directory for the SQLite database exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def get_db_connection():
    """
    Context manager to handle SQLite database connections.
    Yields a connection that can be used to execute queries.
    """
    connection = None
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        yield connection
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
    finally:
        if connection:
            connection.close()

def init_db():
    """
    Initializes the database with the required tables if they don't already exist.
    """
    with get_db_connection() as conn:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS flashcard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    difficulty_level TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS quiz (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    questions TEXT NOT NULL,
                    difficulty_level TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS progress (
                    user_id INTEGER NOT NULL,
                    score INTEGER NOT NULL,
                    level TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES user(id)
                )
            ''')
            conn.commit()

def execute_query(query: str, parameters: List[Any] = []) -> None:
    """
    Executes a given SQL query with optional parameters.
    This function is suitable for 'INSERT', 'UPDATE', 'DELETE' queries.
    """
    try:
        with get_db_connection() as conn:
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute(query, parameters)
                conn.commit()
    except sqlite3.Error as e:
        logging.error(f"An error occurred while executing the query: {e}")

def fetch_query(query: str, parameters: List[Any] = []) -> List[Dict[str, Any]]:
    """
    Executes a given SQL query with optional parameters and returns the results.
    This function is suitable for 'SELECT' queries.
    """
    try:
        with get_db_connection() as conn:
            if conn is not None:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, parameters)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
    except sqlite3.Error as e:
        logging.error(f"An error occurred while fetching the query results: {e}")
        return []

# Initialize the database when this module is imported
init_db()
