from numpy.typing import ArrayLike
from prefect import task
from sklearn.base import BaseEstimator


@task(name="Prediction")
def predict(X: ArrayLike, model: BaseEstimator) -> ArrayLike:
    """Predict the given data using the given model."""
    return model.predict(X)
