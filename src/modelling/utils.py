import os
import pickle
from typing import Union

from loguru import logger
from sklearn.base import BaseEstimator
from sklearn.preprocessing import OneHotEncoder


def pickle_object(object: Union[BaseEstimator, OneHotEncoder], filepath: os.PathLike) -> None:
    """Serialize (pickle) the object to the given filepath."""
    with open(filepath, "wb") as f:
        pickle.dump(object, f)
    logger.info(f"Pickled model to {filepath}")
