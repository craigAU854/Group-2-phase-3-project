# models.py
from sqlalchemy import Column, Integer, String, UniqueConstraint , Float, Date
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
    price = Column(Float)
    area_sqft = Column(Integer)
    size = Column(Integer)
    house_type = Column(String)

class User(Base):
    __tablename__ = 'users'

    __table_args__ = (
        UniqueConstraint('email', name='user_email'),
    )
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String(55))
    no_of_houses = Column(Integer)

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String)
