## Here we will create my database and connect to it
## This will be used for writing my info there

## Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## Variables
SQLALCHEMY_DATABASE_URL = "sqlite:///./raspberryPi.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()