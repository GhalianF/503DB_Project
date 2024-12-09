# app/crud.py
from sqlalchemy.orm import Session
from . import models

def create_car(db: Session, make: str, model: str, year: int):
    """
    Create a new car in the database
    """
    db_car = models.Car(make=make, model=model, year=year)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of cars
    """
    return db.query(models.Car).offset(skip).limit(limit).all()

def create_car_part(db: Session, name: str, description: str, price: float, car_id: int):
    """
    Create a new car part for a specific car
    """
    db_part = models.CarPart(name=name, description=description, price=price, car_id=car_id)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def get_car_parts(db: Session, car_id: int):
    """
    Retrieve parts for a specific car
    """
    return db.query(models.CarPart).filter(models.CarPart.car_id == car_id).all()