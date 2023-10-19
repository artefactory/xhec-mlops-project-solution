from typing import List

from fastapi import FastAPI
from loguru import logger

from config.app_config import APP_DESCRIPTION, APP_TITLE
from src.web_service.lib.models import InputAbaloneData, PredictionOut
from src.web_service.workflows import prediction

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: List[InputAbaloneData]) -> dict:
    logger.info(
        f"Received request to predict {len(payload)} abalone{'' if len(payload) == 1 else 's'}"
    )
    return prediction(payload)
