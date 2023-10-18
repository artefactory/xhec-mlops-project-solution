"""Train a model on the given data."""
from numpy.typing import ArrayLike
from sklearn.base import BaseEstimator
from sklearn.linear_model import LinearRegression


def train_model(X: ArrayLike, y: ArrayLike) -> BaseEstimator:
    """Train a linear regression model on the given data."""
    model = LinearRegression()
    model.fit(X, y)
    return model
