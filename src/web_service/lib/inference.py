from typing import List

import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.preprocessing import OneHotEncoder

from src.web_service.lib.models import InputAbaloneData


def run_inference(
    data: List[InputAbaloneData], model: BaseEstimator, encoder: OneHotEncoder
) -> None:
    """Run inference on the given data using the given model."""
    df = pd.DataFrame([x.dict() for x in data])
    df_cat = encoder.transform(df.select_dtypes(include="object")).toarray()
    df_num = df.select_dtypes(include="number")
    data = pd.concat(
        [df_num, pd.DataFrame(df_cat, columns=encoder.categories_[0].tolist())], axis=1
    )
    prediction = model.predict(data)
    return prediction
