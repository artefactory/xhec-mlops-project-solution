import os
import pickle
from functools import lru_cache

import mlflow
from loguru import logger
from sklearn.base import BaseEstimator


@lru_cache
def load_model(filepath: os.PathLike) -> BaseEstimator:
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)


def load_model_with_mlflow(mlflow_experiment_path: str) -> BaseEstimator:
    logger.info(f"Loading model from MLflow model registry: {mlflow_experiment_path}")
    model_uri = f"models:/{mlflow_experiment_path}/production"
    return mlflow.sklearn.load_model(model_uri)
