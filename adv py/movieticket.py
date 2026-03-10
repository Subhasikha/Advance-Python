shows = {"1": "10:00 AM", "2": "2:00 PM", "3": "6:00 PM"}
seats = ["A1","A2","A3","A4","A5"]

while True:
    print("\n1.Check Showtimes")
    print("2.Book Ticket")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Showtimes:")
        for s in shows:
            print(s, "-", shows[s])

    elif choice == "2":
        show = input("Select show number: ")
        if show in shows:
            print("Available Seats:", seats)
            seat = input("Choose seat: ")
            if seat in seats:
                name = input("Enter your name: ")
                seats.remove(seat)
                print("\nBooking Confirmed!")
                print("Name:", name)
                print("Showtime:", shows[show])
                print("Seat:", seat)
            else:
                print("Seat not available")
        else:
            print("Invalid show")

    elif choice == "3":
        break
