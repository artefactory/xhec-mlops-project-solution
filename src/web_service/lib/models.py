from pydantic import BaseModel


class InputData(BaseModel):
    PULocationID: int
    DOLocationID: int
    passenger_count: int


class PredictionOut(BaseModel):
    predicted_abalone_size: float
