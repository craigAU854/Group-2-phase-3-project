# models.py
from sqlalchemy import Column, Integer, String, UniqueConstraint , Float, desc 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine('sqlite:///houseList.db')
Session = sessionmaker(bind=engine)
session = Session()
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

    users = relationship('User', back_populates='house')
    agents = relationship('Agent', back_populates='house')

    def expensive_house(cls):
        return session.query(cls).order_by(desc(cls.price)).first()
    
    def cheap_house(cls):
        return session.query(cls).order_by((cls.price)).first()
    
    def most_area_sqft(cls):
        return session.query(cls).order_by(desc(cls.area_sqft)).first()
    
    def least_area_sqft(cls):
        return session.query(cls).order_by((cls.area_sqft)).first()
    
    def most_rooms(cls):
        return session.query(cls).order_by(desc(cls.rooms)).first()
    
    def get_rooms(cls):
        return session.query(cls)


class User(Base):
    __tablename__ = 'users'

    __table_args__ = (
        UniqueConstraint('email', name='user_email'),
    )
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey=('house.id'))
    name = Column(String, index=True)
    email = Column(String(55))
    no_of_houses = Column(Integer)

    house = relationship('house', back_populates='users')
    agent = relationship('agent', back_populates='users')

    def most_houses(cls):
        return session.query(cls).order_by(desc(cls.no_of_houses)).first()

    def most_expensive_house(cls):
        return session.query(cls.house).order_by(desc(cls.house.price)).first()

    def least_expensive_house(cls):
        return session.query(cls.house).order_by(cls.house.price).first()
    

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=('user.id'))
    house_id = Column(Integer, ForeignKey=('house.id'))
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String)
    no_of_sold_houses = Column(Integer)

    user = relationship('user', back_populates='agents')
    house = relationship('house', back_populates='agents')
 
    def most_sold_houses(cls):
        return session.query(cls).order_by(desc(cls.no_of_sold_houses)).first()

    def least_sold_houses(cls):
        return session.query(cls).order_by(cls.no_of_sold_houses).first()
# Create tables
Base.metadata.create_all(bind=engine)