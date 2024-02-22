## data_manager.py
import json
from typing import Dict, Optional

class DataManager:
    """Class to handle data loading and saving for the application."""
    
    def load_data(self, file_path: str) -> Optional[Dict]:
        """
        Loads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing the data.

        Returns:
            Optional[dict]: The data loaded from the JSON file or None if an error occurs.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error: The file {file_path} could not be decoded.", doc=e.doc, pos=e.pos) from e

    def save_progress(self, progress_data: Dict, file_path: str = "progress.json") -> None:
        """
        Saves progress data to a JSON file.

        Args:
            progress_data (dict): The progress data to be saved.
            file_path (str, optional): The path to the JSON file where the data should be saved. Defaults to "progress.json".
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(progress_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Error: The file {file_path} could not be written.") from e
