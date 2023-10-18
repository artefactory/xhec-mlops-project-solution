from typing import List

from fastapi import FastAPI
from loguru import logger

from config.app_config import APP_DESCRIPTION, APP_TITLE
from config.config import OBJECTS_PATH
from src.web_service.lib.inference import run_inference
from src.web_service.lib.models import InputAbaloneData, PredictionOut
from src.web_service.utils import load_model

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: List[InputAbaloneData]) -> dict:
    model = load_model(OBJECTS_PATH / "model.pkl")
    encoder = load_model(OBJECTS_PATH / "encoder.pkl")
    logger.info(f"Running inference for {len(payload)} abalone{'' if len(payload) == 1 else 's'}")
    prediction = run_inference(payload, model, encoder)
    return {"predicted_abalone_ages": list(prediction)}
