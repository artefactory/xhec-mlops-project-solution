from enum import Enum
from typing import List

from pydantic import BaseModel


class AbaloneSex(str, Enum):
    male = "M"
    female = "F"
    infant = "I"


class InputAbaloneData(BaseModel):
    sex: AbaloneSex
    length: float
    diameter: float
    height: float
    whole_weight: float
    shucked_weight: float
    viscera_weight: float
    shell_weight: float

    class Config:
        use_enum_values = True


class PredictionOut(BaseModel):
    predicted_abalone_ages: List[float]
    predicted_abalone_ages: List[float]
    predicted_abalone_ages: List[float]
