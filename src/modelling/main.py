from pathlib import Path

import mlflow
import pandas as pd
import typer
from loguru import logger
from mlflow import MlflowClient

from config.config import MLFLOW_TRACKING_URI, OBJECTS_PATH, TARGET
from src.modelling.preprocessing import preprocess
from src.modelling.training import train_model
from src.modelling.utils import pickle_object, save_model_mlflow

app = typer.Typer()


@app.command()
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path."""
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
    logger.info("START")
    with mlflow.start_run() as run:
        logger.info("Processing data...")
        data = pd.read_csv(trainset_path)
        data.columns = [col.replace(" ", "_").lower() for col in data.columns]
        X = data.drop(TARGET, axis=1)
        y = data[TARGET]
        X, encoder = preprocess(X)
        pickle_object(encoder, OBJECTS_PATH / "encoder.pkl")
        logger.info("Training model...")
        model = train_model(X, y)
        # pickle_object(model, OBJECTS_PATH / "model.pkl")
        save_model_mlflow(model, "abalone", run.info.run_id, client)


if __name__ == "__main__":
    app()
