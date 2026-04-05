## This will be where my actual database creation lives
## We will log the Raspberry Pi's temperature, the uptime, and the time it was was currently
## logged at

from sqlalchemy import Column, Float, String, func , DateTime
from database import Base

## classes
class raspberryPiDB(Base):

    __tablename__ = "raspberryPi_info"

    temp = Column(Float)
    uptime = Column(String)
    timeStamp = Column(DateTime(timezone=True) , primary_key= True, server_default=func.now())