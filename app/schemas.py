# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class CarPartBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class CarPartCreate(CarPartBase):
    car_id: int

class CarPartResponse(CarPartBase):
    id: int
    car_id: int

    class Config:
        orm_mode = True

class CarBase(BaseModel):
    make: str
    model: str
    year: int

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int
    parts: List[CarPartResponse] = []

    class Config:
        orm_mode = True