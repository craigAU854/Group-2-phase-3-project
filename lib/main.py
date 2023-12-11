def add_house(house_list):
    print("Add House")
    nHouse = input("Enter name of the house: ")
    print("Location: ")
    nLocation = input("Enter location of the house: ")
    print("Number of rooms: ")
    nRooms = input("Enter number of rooms: ")
    print("Type of house: ")
    nType = input("Enter the type of the house: ")
    print("Size in square feet: ")
    nSize = input("Enter size of the house: ")
    house_list.append([nHouse, nLocation, nRooms, nSize, nType])

def search_house(house_list):
    print("Finding a house...")
    keyword = input("Enter Search Term: ")
    for house in house_list:
        if keyword in house:
            print("\n".join([f"{key}: {value}" for key, value in zip(["Name of house", "Location", "Number of rooms", "Size in square feet", "Type of house"], house)]))
            print()

def display_houses(house_list):
    print("Display all houses...")
    for house in house_list:
        print("\n".join([f"{key}: {value}" for key, value in zip(["Name of house", "Location", "Number of rooms", "Size in square feet", "Type of house"], house)]))
        print()

def main():
    try:
        # initialize house list
        houseList = []
        with open('houseList.db', "r") as infile:
            line = infile.readline().strip()
            while line:
                houseList.append(line.split(","))
                line = infile.readline().strip()

    except FileNotFoundError:
        print("Error finding file.")
        houseList = []

    choice = 0
    while choice != 4:
        print("***Welcome to Amana Realty***")
        print("1) Add a house")
        print("2) Find a house")
        print("3) Show houses")
        print("4) Quit")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            add_house(houseList)

        elif choice == 2:
            search_house(houseList)

        elif choice == 3:
            display_houses(houseList)

        elif choice == 4:
            print("Quitting Program...")

    print('Program Terminated')

    # Saving
    with open("houseList.db", "w") as outfile:
        for house in houseList:
            outfile.write("\n".join([f"{key}: {value}" for key, value in zip(["Name of house", "Location", "Number of rooms", "Size in square feet", "Type of house"], house)]))
            outfile.write("\n\n")

if __name__ == "__main__":
    main()
