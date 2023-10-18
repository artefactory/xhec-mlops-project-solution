from pathlib import Path

import pandas as pd
import typer

from config.config import OBJECTS_PATH, TARGET
from src.modelling.preprocessing import preprocess
from src.modelling.training import train_model
from src.modelling.utils import pickle_object

app = typer.Typer()


@app.command()
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path."""
    data = pd.read_csv(trainset_path)
    data.columns = [col.replace(" ", "_").lower() for col in data.columns]
    X = data.drop(TARGET, axis=1)
    y = data[TARGET]
    X, encoder = preprocess(X)
    pickle_object(encoder, OBJECTS_PATH / "encoder.pkl")
    model = train_model(X, y)
    pickle_object(model, OBJECTS_PATH / "model.pkl")


if __name__ == "__main__":
    app()
