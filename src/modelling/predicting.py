from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator


def predict(X: ArrayLike, model: BaseEstimator) -> ArrayLike:
    """Predict the given data using the given model."""
    return model.predict(X)
