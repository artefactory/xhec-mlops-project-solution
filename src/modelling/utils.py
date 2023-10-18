import os
import pickle

from loguru import logger
from sklearn.base import BaseEstimator


def pickle_model(model: BaseEstimator, filepath: os.PathLike) -> None:
    """Serialize (pickle) the model to the given filepath."""
    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    logger.info(f"Pickled model to {filepath}")
