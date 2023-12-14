
# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///houseList.db')

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    rooms = Column(Integer)
    size = Column(Integer)
    house_type = Column(String)