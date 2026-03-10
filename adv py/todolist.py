tasks = []

while True:
    print("\n1.Add Task")
    print("2.View All Tasks")
    print("3.Filter by Project")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Task name: ")
        deadline = input("Deadline: ")
        priority = input("Priority (High/Medium/Low): ")
        project = input("Project/Tag: ")

        task = {
            "name": name,
            "deadline": deadline,
            "priority": priority,
            "project": project
        }

        tasks.append(task)
        print("Task added")

    elif choice == "2":
        print("\nAll Tasks:")
        for t in tasks:
            print(t["name"], "| Deadline:", t["deadline"], "| Priority:", t["priority"], "| Project:", t["project"])

    elif choice == "3":
        p = input("Enter project/tag: ")
        print("\nFiltered Tasks:")
        for t in tasks:
            if t["project"] == p:
                print(t["name"], "| Deadline:", t["deadline"], "| Priority:", t["priority"])

    elif choice == "4":
        break
