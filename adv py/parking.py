capacity = 10
parking = {}

while True:
    print("\n1.Vehicle Entry")
    print("2.Vehicle Exit")
    print("3.Available Spots")
    print("4.Exit Program")

    choice = input("Enter choice: ")

    if choice == "1":
        if len(parking) < capacity:
            vehicle = input("Enter vehicle number: ")
            time = int(input("Enter entry time (hour): "))
            parking[vehicle] = time
            print("Vehicle parked")
        else:
            print("Parking Full")

    elif choice == "2":
        vehicle = input("Enter vehicle number: ")
        if vehicle in parking:
            exit_time = int(input("Enter exit time (hour): "))
            hours = exit_time - parking[vehicle]
            fee = hours * 10
            print("Parking Fee:", fee)
            del parking[vehicle]
        else:
            print("Vehicle not found")

    elif choice == "3":
        print("Available spots:", capacity - len(parking))

    elif choice == "4":
        break
