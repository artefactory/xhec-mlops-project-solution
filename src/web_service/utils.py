import os
import pickle
from functools import lru_cache

from loguru import logger
from sklearn.base import BaseEstimator


@lru_cache
def load_object(filepath: os.PathLike) -> BaseEstimator:
    """Load a pickled object from the given filepath."""
    logger.info(f"Loading object from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)
