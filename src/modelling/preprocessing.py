import pandas as pd
from numpy.typing import ArrayLike
from prefect import task
from sklearn.preprocessing import OneHotEncoder


@task(name="Preprocessing")
def preprocess(X: ArrayLike) -> pd.DataFrame:
    """Preprocess the given data."""
    encoder = OneHotEncoder(handle_unknown="ignore")
    X_cat = encoder.fit_transform(X.select_dtypes(include="object")).toarray()
    X_num = X.select_dtypes(include="number")
    data = pd.concat([X_num, pd.DataFrame(X_cat, columns=encoder.categories_[0].tolist())], axis=1)
    return data, encoder
    return data, encoder
