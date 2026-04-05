## This will be for my pydantic data verification
## It will verify that the temp number is a floating point number
## And it will then add the uptime to the database
## with a timestamp

from pydantic import BaseModel, Field
from datetime import datetime

## Our verification

class raspberryPi(BaseModel):
    temp: float
    uptime: str = Field(min_length=3, max_length=10)
    timeStamp: datetime
