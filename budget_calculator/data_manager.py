"""Module for handling data operations in the Budget Calculator."""

import json
import datetime
from pathlib import Path
from typing import Dict, Any

from .config import DEFAULT_DATA, DATA_FILE

class DataManager:
    """Handles all data operations for the Budget Calculator."""
    
    @staticmethod
    def load_data() -> Dict[str, Any]:
        """Load data from the JSON file, create with defaults if it doesn't exist."""
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            DataManager.save_data(DEFAULT_DATA)
            return DEFAULT_DATA.copy()
    
    @staticmethod
    def save_data(data: Dict[str, Any]) -> None:
        """Save the current data to the JSON file."""
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=2)
    
    @staticmethod
    def export_data(data: Dict[str, Any]) -> str:
        """Export the current data to a timestamped JSON file."""
        timestamp = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
        export_file = f'{timestamp}.json'
        
        with open(export_file, 'w') as file:
            json.dump(data, file, indent=2)
        
        return export_file
    
    @staticmethod
    def str_to_float(value: str) -> float:
        """Convert string to float, return 0.0 if invalid."""
        try:
            return float(value)
        except ValueError:
            return 0.0 