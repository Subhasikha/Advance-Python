students = {}

while True:
    print("\n1.Enter Marks")
    print("2.View Result")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        m1 = int(input("Marks in Subject 1: "))
        m2 = int(input("Marks in Subject 2: "))
        m3 = int(input("Marks in Subject 3: "))

        avg = (m1 + m2 + m3) / 3
        gpa = avg / 25

        students[name] = gpa
        print("Marks recorded")

    elif choice == "2":
        for s in students:
            print("Student:", s, "| GPA:", round(students[s],2))

    elif choice == "3":
        break
