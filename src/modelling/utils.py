import os
import pickle
from typing import Union

import mlflow
from loguru import logger
from mlflow.tracking import MlflowClient
from sklearn.base import BaseEstimator
from sklearn.preprocessing import OneHotEncoder


def pickle_object(object: Union[BaseEstimator, OneHotEncoder], filepath: os.PathLike) -> None:
    """Serialize (pickle) the object to the given filepath."""
    with open(filepath, "wb") as f:
        pickle.dump(object, f)
    logger.info(f"Pickled model to {filepath}")


def save_model_mlflow(
    model: BaseEstimator,
    model_name: str,
    run_id: str,
    client: MlflowClient,
    production_version: int = 1,
) -> None:
    """Save the given model to the MLflow model registry."""
    mlflow.sklearn.log_model(model, "models")
    mlflow.register_model(f"runs:/{run_id}/models", model_name)
    client.transition_model_version_stage(
        name=model_name, version=production_version, stage="Production"
    )
