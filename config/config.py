"""Module for dynamic configuration variables of the project."""
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
OBJECTS_PATH = ROOT_PATH / "src/web_service/local_objects"
TARGET = "rings"
