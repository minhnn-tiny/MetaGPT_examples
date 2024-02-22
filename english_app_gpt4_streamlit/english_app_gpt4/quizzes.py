## quizzes.py
import json
from typing import List, Dict
from data_manager import DataManager

class Quiz:
    def __init__(self, questions: List[Dict[str, str]]):
        self.questions = questions

    def evaluate_answers(self, answers: List[str]) -> int:
        score = 0
        for question, answer in zip(self.questions, answers):
            if question['correct_answer'].lower() == answer.lower():
                score += 1
        return score

class Quizzes:
    def __init__(self):
        self.quizzes = []
        self.current_quiz_index = 0

    def load_quizzes(self) -> None:
        try:
            data_manager = DataManager()
            quizzes_data = data_manager.load_data('quizzes.json')
            self.quizzes = []
            for quiz in quizzes_data:
                if 'questions' in quiz and all('correct_answer' in question for question in quiz['questions']):
                    self.quizzes.append(Quiz(quiz['questions']))
                else:
                    print(f"Skipping invalid quiz data: {quiz}")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading quizzes: {e}")
            self.quizzes = []

    def get_quiz(self) -> Quiz:
        if not self.quizzes:
            self.load_quizzes()
        if self.quizzes:  # Check if quizzes are loaded successfully
            quiz = self.quizzes[self.current_quiz_index]
            self.current_quiz_index = (self.current_quiz_index + 1) % len(self.quizzes)
            return quiz
        else:
            raise ValueError("No quizzes available.")

    def reload_quizzes(self) -> None:
        self.load_quizzes()
        self.current_quiz_index = 0
