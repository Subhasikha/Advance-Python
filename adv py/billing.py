products = {"rice": 50, "milk": 30, "bread": 25, "eggs": 10}
transactions = []

while True:
    print("\n1.New Bill")
    print("2.View Transactions")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        total = 0
        while True:
            item = input("Enter product name (or done): ")
            if item == "done":
                break
            if item in products:
                qty = int(input("Enter quantity: "))
                price = products[item] * qty
                total += price
            else:
                print("Product not found")

        discount = int(input("Enter discount (%): "))
        final = total - (total * discount / 100)

        print("Total:", total)
        print("Final Bill:", final)

        transactions.append(final)

    elif choice == "2":
        print("Transactions:", transactions)

    elif choice == "3":
        break
