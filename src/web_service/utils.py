import os
import pickle
from functools import lru_cache

from loguru import logger
from sklearn.base import BaseEstimator


@lru_cache
def load_model(filepath: os.PathLike) -> BaseEstimator:
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)
