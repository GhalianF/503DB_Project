# main.py
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
import os

from app.database import engine, Base, get_db
from app import models, crud, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Prepare templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Root route serving the main HTML page
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cars/", response_model=schemas.CarResponse)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new car
    """
    return crud.create_car(db=db, make=car.make, model=car.model, year=car.year)

@app.get("/cars/", response_model=List[schemas.CarResponse])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve cars
    """
    return crud.get_cars(db, skip=skip, limit=limit)

@app.post("/parts/", response_model=schemas.CarPartResponse)
def create_part(part: schemas.CarPartCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new car part
    """
    return crud.create_car_part(
        db=db, 
        name=part.name, 
        description=part.description, 
        price=part.price, 
        car_id=part.car_id
    )

@app.get("/cars/{car_id}/parts/", response_model=List[schemas.CarPartResponse])
def read_car_parts(car_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve parts for a specific car
    """
    return crud.get_car_parts(db, car_id=car_id)