from typing import List

from pydantic import BaseModel


class InputAbaloneData(BaseModel):
    sex: str
    length: float
    diameter: float
    height: float
    whole_weight: float
    shucked_weight: float
    viscera_weight: float
    shell_weight: float


class PredictionOut(BaseModel):
    predicted_abalone_ages: List[float]
