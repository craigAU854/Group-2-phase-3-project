# display.py
from models import House

def display_house_info(house):
    print("\n".join(f"{key}: {getattr(house, key)}" for key in House.__table__.columns.keys()))
    print()

def display_houses(houses):
    for house in houses:
        display_house_info(house)
