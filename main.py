## This will be where my main script lives
## From here we will grab the data
## and then after grabbing said data, we will put it into a database

## Imports

from pi_data import raspberry_pi_data
from fastapi import FastAPI , Depends , Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

## Variables
app = FastAPI()
app.mount("/static" , StaticFiles(directory="static") , name="static")
templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)

## functions

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_to_db(db: Session, data_dict: dict):
    db_info = models.raspberryPiDB(**data_dict)
    db.add(db_info)
    db.commit()
    return db_info

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    my_device = raspberry_pi_data()

    cpu_temp = "N/A"
    uptime = "N/A"

    ## If we can connect to the device, log to database, and show on screen
    if my_device.connected:
        my_device.hw_data()
        cpu_temp = my_device.cpu_temp
        uptime = my_device.uptime
        
        info_to_save = {
            "temp": cpu_temp, 
            "uptime": uptime
        }
        add_to_db(db, info_to_save) 

    return templates.TemplateResponse(
    request=request, 
    name="home.html", 
    context={
        "cpu_temp": cpu_temp, 
        "uptime": uptime
    }
)

