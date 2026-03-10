warehouse = {}
def add_goods(name, quantity, price):
    warehouse[name] = {
        "quantity": quantity,
        "price": price
    }
    print(f"{name} added/updated successfully.")
def track_goods():
    if not warehouse:
        print("Warehouse is empty.")
        return
    print("\nAvailable Goods:")
    for item, details in warehouse.items():
        print(f"Item: {item}, Quantity: {details['quantity']}, Price: ${details['price']}")
def check_availability(name):
    if name in warehouse:
        print(f"{name} is available. Quantity: {warehouse[name]['quantity']}")
    else:
        print(f"{name} is not available in warehouse.")
def check_price(name):
    if name in warehouse:
        print(f"Price of {name}: ${warehouse[name]['price']}")
    else:
        print(f"{name} not found in warehouse.")
def main():
    while True:
        print("\n--- Warehouse Management System ---")
        print("1. Add Goods")
        print("2. Track Goods")
        print("3. Check Availability")
        print("4. Check Price")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_goods(name, quantity, price)
        elif choice == "2":
            track_goods()
        elif choice == "3":
            name = input("Enter item name to check availability: ")
            check_availability(name)
        elif choice == "4":
            name = input("Enter item name to check price: ")
            check_price(name)
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
