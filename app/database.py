# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database (you can change to another database if needed)
DATABASE_URL = "sqlite:///./car_parts.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

def get_db():
    """
    Dependency that creates a new database session for each request
    and closes it after the request is completed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()