from models import House, User, Agent, Base, engine, Session  # Import Session instead of session

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data():
    # House data
    house_data = [
        {'name': 'House 1', 'location': 'Nairobi', 'rooms': 3, 'price': 200000.0, 'area_sqft': 1500, 'size': 5, 'house_type': 'Single-Family'},
        {'name': 'House 2', 'location': 'nakuru', 'rooms': 4, 'price': 250000.0, 'area_sqft': 1800, 'size': 6, 'house_type': 'Duplex'},
        # Add more house data as needed
    ]

    # User data 
    user_data = [
        {'name': 'John Doe', 'email': 'johndoe@example.com', 'no_of_houses': 2},
        {'name': 'Jane Smith', 'email': 'janesmith@example.com', 'no_of_houses': 1},
        # Add more user data as needed
    ]

    # Agent data
    agent_data = [
        {'name': 'Paul', 'email': 'paul@example.com', 'phone_number': '123-456-7890', 'no_of_sold_houses': 5},
        {'name': 'David', 'email': 'david2@example.com', 'phone_number': '987-654-3210', 'no_of_sold_houses': 3},
        # Add more agent data as needed
    ]

    # Seed houses
    for data in house_data:
        house = House(**data)
        Session.add(house)  # Use Session instead of session

    # Seed users
    for data in user_data:
        user = User(**data)
        Session.add(user)  # Use Session instead of session

    # Seed agents
    for data in agent_data:
        agent = Agent(**data)
        Session.add(agent)  # Use Session instead of session

    # Commit the changes
    Session.commit()  # Use Session instead of session

if __name__ == "__main__":
    seed_data()
