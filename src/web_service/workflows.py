from typing import List

from prefect import flow

from config.config import OBJECTS_PATH
from src.web_service.lib.inference import run_inference
from src.web_service.lib.models import InputAbaloneData
from src.web_service.utils import load_object


@flow(name="Predict Abalone Age")
def prediction(payload: List[InputAbaloneData]) -> dict:
    model = load_object(OBJECTS_PATH / "model.pkl")
    encoder = load_object(OBJECTS_PATH / "encoder.pkl")
    prediction = run_inference(payload, model, encoder)
    return {"predicted_abalone_ages": list(prediction)}
