customers = {}
logs = {}
sales = {}

while True:
    print("\n1.Add Customer")
    print("2.Add Communication Log")
    print("3.Add Sales Pipeline")
    print("4.Show Customers")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Customer name: ")
        email = input("Email: ")
        customers[name] = email
        print("Customer added")

    elif choice == "2":
        name = input("Customer name: ")
        message = input("Communication note: ")
        logs.setdefault(name, []).append(message)
        print("Log saved")

    elif choice == "3":
        name = input("Customer name: ")
        stage = input("Sales stage (lead/deal/closed): ")
        sales[name] = stage
        print("Sales stage updated")

    elif choice == "4":
        print("\nCustomer Details:")
        for c in customers:
            print("Name:", c, "| Email:", customers[c], "| Stage:", sales.get(c,"None"))

    elif choice == "5":
        break
