freelancers = []
clients = []
projects = []
while True:
    print("\n1.Register Freelancer")
    print("2.Register Client")
    print("3.Assign Project")
    print("4.Process Payment")
    print("5.Show Projects")
    print("6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Freelancer name: ")
        freelancers.append(name)
        print("Freelancer registered")
    elif choice == "2":
        name = input("Client name: ")
        clients.append(name)
        print("Client registered")
    elif choice == "3":
        client = input("Client name: ")
        freelancer = input("Freelancer name: ")
        project = input("Project title: ")
        projects.append((client, freelancer, project))
        print("Project assigned")
    elif choice == "4":
        freelancer = input("Freelancer name: ")
        amount = input("Payment amount: ")
        print("Payment of", amount, "paid to", freelancer)
    elif choice == "5":
        for p in projects:
            print("Client:", p[0], "| Freelancer:", p[1], "| Project:", p[2])
    elif choice == "6":
        break
