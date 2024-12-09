# app/forms.py
from typing import Optional
from pydantic import BaseModel

class CarCreate(BaseModel):
    """
    Pydantic model for car creation
    """
    make: str
    model: str
    year: int

class CarPartCreate(BaseModel):
    """
    Pydantic model for car part creation
    """
    name: str
    description: Optional[str] = None
    price: float
    car_id: int