from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


BaseModel = declarative_base()


class Temp(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
