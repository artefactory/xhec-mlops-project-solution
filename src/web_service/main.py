from fastapi import FastAPI

from config.app_config import APP_DESCRIPTION, APP_TITLE
from src.web_service.lib.models import InputData, PredictionOut

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION)


@app.get("/")
def home() -> dict:
    return {"health_check": "OK"}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData) -> dict:  # noqa ARG001
    return {"predicted_abalone_size": 2}
