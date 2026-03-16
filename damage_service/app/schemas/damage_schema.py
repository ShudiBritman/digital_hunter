from pydantic import BaseModel
from datetime import datetime



class DamageSignal(BaseModel):
    timestamp: datetime
    attack_id: str
    entity_id: str
    result: str