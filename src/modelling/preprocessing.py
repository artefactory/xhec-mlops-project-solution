import pandas as pd
from numpy.typing import ArrayLike


def preprocess(X: ArrayLike) -> pd.DataFrame:
    """Preprocess the given data."""
    return pd.get_dummies(X)
