student ={}
while True:
    print("/n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. Check Student")
    print("3. Check Rsult")
    print("4. Exit")

    choice=input("Enter your choice: ")
    #Add Student 
    if choice == "1":
        name=input("Enter student name: ")
        marks=int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} Successfully Added")
    #Check Student
    elif choice == "2":
        if not student:
            print("Student not found")
        else:
            for name,marks in student.items():
                print(name, ":", marks)
    #Check Result
    elif choice == "3":
        name=input("Enter student name: ")
        if name in student:
            marks=student[name]
            if marks > 33 :
                print("PASS :)")
            else:
                print("FAIL!")
        else:
            print("Student not found")
    elif choice =="4":
        print("EXiting...")
        break
    else:
        print("Invalid Input")

    