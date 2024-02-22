## services.py
import logging
from typing import List, Optional
from datetime import datetime, timedelta
from models import User, Flashcard, Quiz, Progress
from database import DatabaseSession

class AdaptiveLearningService:
    """
    Implements the adaptive learning logic, including the spaced repetition algorithm.
    This service adjusts the learning path based on the user's progress and the principles of spaced repetition.
    """
    
    def __init__(self, db_session: DatabaseSession):
        self.db_session = db_session

    def calculate_next_session_date(self, score: int, last_session_date: datetime, difficulty: str, historical_performance: List[int]) -> datetime:
        """
        Calculates the next session date based on the user's score, the last session date, difficulty of the content, and historical performance.
        
        :param score: The score obtained in the latest learning session.
        :param last_session_date: The date of the last learning session.
        :param difficulty: The difficulty level of the content.
        :param historical_performance: A list of scores representing the user's historical performance.
        :return: A datetime object representing the next session date.
        """
        # Example logic for adjusting interval based on difficulty and historical performance
        base_interval = { 'Easy': 7, 'Medium': 5, 'Hard': 3 }
        performance_factor = sum(historical_performance) / len(historical_performance) if historical_performance else score
        interval = base_interval.get(difficulty, 5) - (performance_factor // 10)
        interval = max(1, interval)  # Ensure interval is at least 1 day
        return last_session_date + timedelta(days=int(interval))
    
    def adjust_learning_path(self, user_progress: Progress) -> List[str]:
        """
        Adjusts the learning path for the user based on their progress and the principles of spaced repetition.
        
        :param user_progress: Progress object containing the user's learning progress.
        :return: A list of recommended topics or areas for the user to focus on.
        """
        level = user_progress.get_level()
        recommendations = {
            'Beginner': ['Basics', 'Introduction to Verbs'],
            'Intermediate': ['Intermediate Grammar', 'Vocabulary Expansion'],
            'Advanced': ['Advanced Conversations', 'Complex Grammar'],
        }
        return recommendations.get(level, ['General Revision'])
    
    def update_user_progress(self, user_id: int, score: int) -> None:
        """
        Updates the user's progress based on the latest quiz or flashcard session score and calculates the next session date.
        
        :param user_id: The ID of the user whose progress is being updated.
        :param score: The score obtained in the latest learning session.
        """
        try:
            progress: Optional[Progress] = self.db_session.get_progress_by_user_id(user_id)
            if progress:
                progress.update_score(score)
                # Example historical performance data, would need to be fetched or calculated
                historical_performance = [80, 85, 90]  # Placeholder for actual historical performance data
                next_session_date = self.calculate_next_session_date(score, datetime.now(), progress.get_level(), historical_performance)
                progress.next_session_date = next_session_date
                self.db_session.commit_changes()
            else:
                logging.warning(f"No progress found for user ID {user_id}. Unable to update.")
        except Exception as e:
            logging.error(f"Error updating progress for user ID {user_id}: {e}")

# Assuming DatabaseSession is a context manager handling the session lifecycle
def get_adaptive_learning_path(user_id: int) -> List[str]:
    """
    Public function to get the adaptive learning path for a specific user based on the principles of spaced repetition.
    
    :param user_id: The ID of the user for whom to adjust the learning path.
    :return: A list of recommended learning topics.
    """
    with DatabaseSession() as db_session:
        user_progress = db_session.get_progress_by_user_id(user_id)
        if user_progress:
            adaptive_service = AdaptiveLearningService(db_session)
            return adaptive_service.adjust_learning_path(user_progress)
        else:
            logging.warning(f"No progress found for user ID {user_id}. Unable to provide a learning path.")
            return []
