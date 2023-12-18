
# main.py
from database import init_db
from user_input import get_int_input, get_str_input
from display import display_houses
from models import House
from sqlalchemy import desc

def add_house(session):
    print("Add House")
    nHouse = get_str_input("Enter name of the house: ")
    nLocation = get_str_input("Enter location of the house: ")
    nRooms = get_int_input("Enter number of rooms: ")
    nPrice = get_int_input("Enter price of the house: ")
    nSize = get_int_input("Enter size of the house: ")
    nType = get_str_input("Enter the type of the house: ")

    new_house = House(name=nHouse, location=nLocation, rooms=nRooms, price=nPrice, size=nSize, house_type=nType)
    session.add(new_house)
    session.commit()

def search_house(session):
    print("Finding a house...")
    keyword = get_str_input("Enter Search Term: ")
    houses = session.query(House).filter(House.name.like(f"%{keyword}%")).all()
    display_houses(houses)

def delete_house(session):
    print("Delete a house...")
    house_id = get_int_input("Enter the ID of the house you want to delete: ")
    house = session.query(House).filter_by(id=house_id).first()
    if house:
        session.delete(house)
        session.commit()
        print("House deleted successfully.")
    else:
        print("House not found.")

def sort_houses(session):
    print("Sorting houses by size...")
    houses = session.query(House).order_by(desc(House.size)).all()
    display_houses(houses)

def main():
    session = init_db()

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
            choice = get_int_input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            add_house(session)

        elif choice == 2:
            search_house(session)

        elif choice == 3:
            houses = session.query(House).all()
            display_houses(houses)

        elif choice == 4:
            delete_house(session)

        elif choice == 5:
            sort_houses(session)

        elif choice == 6:
            print("Quitting Program...")
    print('Program Terminated')

if __name__ == "__main__":
    main()