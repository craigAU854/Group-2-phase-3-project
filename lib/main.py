from database import init_db
from user_input import get_int_input, get_str_input
from display import display_houses, display_house_info
from models import House
from user import User
from agent import Agent
from sqlalchemy import desc

def add_user(session):
    print("Add User")
    username = get_str_input("Enter username: ")
    email = get_str_input("Enter email: ")
    password = get_str_input("Enter password: ")

    new_user = User(username=username, email=email, password=password)
    session.add(new_user)
    session.commit()

def add_agent(session):
    print("Add Agent")
    name = get_str_input("Enter agent's name: ")
    email = get_str_input("Enter agent's email: ")
    phone = get_str_input("Enter agent's phone number: ")

    new_agent = Agent(name=name, email=email, phone=phone)
    session.add(new_agent)
    session.commit()

def add_house(session):
    print("Add House")
    nHouse = get_str_input("Enter name of the house: ")
    nLocation = get_str_input("Enter location of the house: ")
    nRooms = get_int_input("Enter number of rooms: ")
    nSize = get_int_input("Enter size of the house: ")
    nType = get_str_input("Enter the type of the house: ")

    new_house = House(name=nHouse, location=nLocation, rooms=nRooms, size=nSize, house_type=nType)
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
    while choice != 8:
        print("***Welcome to Amana Realty***")
        print("1) Add a house")
        print("2) Find a house")
        print("3) Show houses")
        print("4) Delete a house")
        print("5) Sort houses by size")
        print("6) Add a user")
        print("7) Add an agent")
        print("8) Quit")

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
            add_user(session)

        elif choice == 7:
            add_agent(session)

        elif choice == 8:
            print("Quitting Program...")
            break

    print('Program Terminated')

if __name__ == "__main__":
    main()
