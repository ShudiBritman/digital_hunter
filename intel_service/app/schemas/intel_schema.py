from pydantic import BaseModel, Field
from typing import Literal, Union, Annotated
from datetime import datetime


range_value = Annotated[int, 
                        Field(gt=0, le=5)]

class IntelSignal(BaseModel):
    timestamp:datetime
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: Literal["SIGINT", "VISINT", "HUMINT"]
    priority_level: Union[range_value, Literal[99]]


    