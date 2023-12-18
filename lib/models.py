from sqlalchemy import Column, Integer, String, UniqueConstraint, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

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

class User(Base):
    __tablename__ = 'users'

    __table_args__ = (
        UniqueConstraint('email', name='user_email'),
    )
    id = Column(Integer, primary_key=True)
    house_id = Column(Integer, ForeignKey('houses.id'))
    name = Column(String, index=True)
    email = Column(String(55), index=True, unique=True)
    no_of_houses = Column(Integer)

    house = relationship('House', back_populates='users')
    agent = relationship('Agent', back_populates='user')

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    house_id = Column(Integer, ForeignKey('houses.id'))
    name = Column(String)
    email = Column(String(55))
    phone_number = Column(String)
    no_of_sold_houses = Column(Integer)

    user = relationship('User', back_populates='agent')
    house = relationship('House', back_populates='agents')

    @classmethod
    def get_sold_houses_count(cls, session, agent_id):
        agent = session.query(cls).filter_by(id=agent_id).first()
        if agent:
            return agent.no_of_sold_houses
        else:
            return 0

# Create tables
Base.metadata.create_all(bind=engine)
