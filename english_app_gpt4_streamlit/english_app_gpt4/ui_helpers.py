## ui_helpers.py
import streamlit as st
from flashcards import Flashcards
from quizzes import Quizzes
from data_manager import DataManager

class StreamlitUI:
    def __init__(self):
        self.flashcards = Flashcards()
        self.quizzes = Quizzes()
        self.data_manager = DataManager()

    def display_home(self):
        st.title("Welcome to the English Learning App!")
        st.write("Select an option from the sidebar to get started.")
        st.sidebar.title("Navigation")
        options = ["Home", "Flashcards", "Quizzes", "Progress"]
        choice = st.sidebar.selectbox("Choose an option", options)

        if choice == "Flashcards":
            self.display_flashcards()
        elif choice == "Quizzes":
            self.display_quizzes()
        elif choice == "Progress":
            self.display_progress()

    def display_flashcards(self):
        st.header("Flashcards")
        st.write("Here you can practice your vocabulary with flashcards.")
        flashcard = self.flashcards.get_random_flashcard()
        if flashcard:
            st.subheader(flashcard.term)
            if st.button("Show Definition"):
                st.write(flashcard.definition)
        else:
            st.write("No flashcards available.")

    def display_quizzes(self):
        st.header("Quizzes")
        st.write("Test your knowledge with quizzes.")
        quiz = self.quizzes.get_quiz()
        if quiz:
            self._display_quiz_questions(quiz)

    def _display_quiz_questions(self, quiz):
        question_number = 1
        user_answers = []
        for question in quiz.questions:
            st.subheader(f"Question {question_number}")
            st.write(question["question"])
            options = question["options"]
            answer = st.radio(f"Select an option for question {question_number}", options, key=question_number)
            user_answers.append(answer)
            question_number += 1

        if st.button("Submit Answers"):
            self._evaluate_quiz_answers(quiz, user_answers)

    def _evaluate_quiz_answers(self, quiz, user_answers):
        score = quiz.evaluate_answers(user_answers)
        st.write(f"Your score: {score}/{len(quiz.questions)}")

    def display_progress(self):
        st.header("Your Progress")
        progress_data = self.data_manager.get_progress()
        if progress_data:
            st.write(f"Your current progress score is {progress_data['score']} out of {progress_data['total']}.")
            progress_percentage = progress_data['score'] / progress_data['total'] * 100
            st.progress(progress_percentage)
        else:
            st.write("No progress data available.")
