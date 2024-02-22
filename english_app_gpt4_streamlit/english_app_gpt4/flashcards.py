## flashcards.py
import json
from typing import List, Optional, Dict

class Flashcard:
    """
    Represents a single flashcard with a term and its definition.
    """
    def __init__(self, term: str, definition: str) -> None:
        self.term = term
        self.definition = definition

class Flashcards:
    """
    Manages the collection of flashcards.
    """
    def __init__(self) -> None:
        self.flashcards: List[Flashcard] = []

    def load_flashcards(self, data_manager) -> None:
        """
        Loads flashcards from a JSON file using the DataManager.
        
        Args:
            data_manager: The DataManager instance used for loading the flashcards data.
        """
        data: Dict = data_manager.load_data('flashcards.json')
        self.flashcards = [Flashcard(flashcard['term'], flashcard['definition']) for flashcard in data.get('flashcards', [])]

    def get_random_flashcard(self) -> Optional[Flashcard]:
        """
        Returns a random flashcard from the collection.

        Returns:
            A random Flashcard object if the collection is not empty, else None.
        """
        if not self.flashcards:
            return None
        from random import choice
        return choice(self.flashcards)
