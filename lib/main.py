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
        houseList=[]

    choice = 0
    while choice != 4:
        print("***Welcome to Amana Realty***")
        print("1) Add a house")
        print("2) Find a house")
        print("3) Show houses")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Add House")
            nHouse = input("Enter name of the house: ")
            print("Location")
            nLocation = input("Enter location of the house: ")
            print("Number of rooms")
            nRooms = input("Enter number of rooms: ")
            print("Type of house")
            nType = input("Enter the type of the house: ")
            print("Size in square feet")
            nSize = input("Enter size of the house: ")
            houseList.append([nHouse, nLocation, nRooms, nSize, nType])

        elif choice == 2:
            print("Finding a house...")
            keyword = input("Enter Search Term: ")
            for house in houseList:
                if keyword in house:
                    print(house)

        elif choice == 3:
            print("Display all houses...")
            for i in range(len(houseList)):
                print(houseList[i])

        elif choice == 4:
            print("Quitting Program...")

    print('Program Terminated')

    # Saving
    with open("houseList.db", "w") as outfile:
        for house in houseList:
            outfile.write(",".join(house) + "\n")

if __name__ == "__main__":
    main()
