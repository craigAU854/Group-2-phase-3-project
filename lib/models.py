# models.py
from sqlalchemy import Column, Integer, String, UniqueConstraint , Float, desc , relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

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

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=('user.id'))
    house_id = Column(Integer, ForeignKey=('house.id'))
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String)

    user = relationship('user', back_populates='agents')
    house = relationship('house', back_populates='agents')

# Create tables
Base.metadata.create_all(bind=engine)