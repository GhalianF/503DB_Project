# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Car(Base):
    """
    Car model representing vehicle information
    """
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    
    # Relationship to parts
    parts = relationship("CarPart", back_populates="car")

class CarPart(Base):
    """
    CarPart model representing individual parts
    """
    __tablename__ = "car_parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    car_id = Column(Integer, ForeignKey("cars.id"))
    
    # Relationship to car
    car = relationship("Car", back_populates="parts")