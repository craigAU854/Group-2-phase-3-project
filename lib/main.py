# main.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    rooms = Column(Integer)
    size = Column(Integer)
    house_type = Column(String)

def create_tables(engine):
    Base.metadata.create_all(engine)

def add_house(session):
    print("Add House")
    nHouse = input("Enter name of the house: ")
    nLocation = input("Enter location of the house: ")
    nRooms = int(input("Enter number of rooms: "))
    nSize = int(input("Enter size of the house: "))
    nType = input("Enter the type of the house: ")

    new_house = House(name=nHouse, location=nLocation, rooms=nRooms, size=nSize, house_type=nType)
    session.add(new_house)
    session.commit()

def search_house(session):
    print("Finding a house...")
    keyword = input("Enter Search Term: ")
    houses = session.query(House).filter(House.name.like(f"%{keyword}%")).all()
    for house in houses:
        print("\n".join(f"{key}: {getattr(house, key)}" for key in House.__table__.columns.keys()))
        print()

def display_houses(session):
    print("Display all houses...")
    houses = session.query(House).all()
    for house in houses:
        print("\n".join(f"{key}: {getattr(house, key)}" for key in House.__table__.columns.keys()))
        print()

def delete_house(session):
    print("Delete a house...")
    house_id = int(input("Enter the ID of the house you want to delete: "))
    house = session.query(House).filter_by(id=house_id).first()
    if house:
        session.delete(house)
        session.commit()
        print("House deleted successfully.")
    else:
        print("House not found.")

def sort_houses(session):
    print("Sorting houses by size...")
    houses = session.query(House).order_by(House.size).all()
    for house in houses:
        print("\n".join(f"{key}: {getattr(house, key)}" for key in House.__table__.columns.keys()))
        print()

def main():
    engine = create_engine('sqlite:///houseList.db', echo=True)
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    choice = 0
    while choice != 6:
        print("***Welcome to Amana Realty***")
        print("1) Add a house")
        print("2) Find a house")
        print("3) Show houses")
        print("4) Delete a house")
        print("5) Sort houses by size")
        print("6) Quit")

        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            add_house(session)

        elif choice == 2:
            search_house(session)

        elif choice == 3:
            display_houses(session)

        elif choice == 4:
            delete_house(session)

        elif choice == 5:
            sort_houses(session)

        elif choice == 6:
            print("Quitting Program...")

    print('Program Terminated')

if __name__ == "__main__":
    main()
