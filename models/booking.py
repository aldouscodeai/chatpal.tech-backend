from pydantic import BaseModel
from typing import Optional

class Booking(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    service: str
    slot: str
    notes: Optional[str] = None
    

    