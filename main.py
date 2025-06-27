import json

'''
Enter 1 to Add student report
Enter 2 to View student report
Enter 3 to Update student report
Enter 4 to View all student name
Enter 5 Exit
'''
while True:
    print('''
    Student Record System:
          Enter 1 to Add student report-->
          Enter 2 to View student report-->
          Enter 3 to Update student report-->
          Enter 4 to View all student name-->
          Enter 5 Exit-->

    ''')

    try:
        UserChoice = int(input("Enter Your Choice:"))
    except ValueError:
        raise ValueError("INVALID!!!! Enter integer")
    
    if UserChoice == 5:
        print("Exiting.....")
        break

    elif UserChoice == 1:
        try:
            name = input("Enter the name: ")
            Class = input("Enter the class: ")
            RollNumber = int(input("Enter the RollNumber: "))
            Physics = int(input("Enter the Physics marks: "))
            Chemistry = int(input("Enter the Chemistry marks: "))
            Maths = int(input("Enter the Maths marks: "))
            Average = (Physics + Chemistry + Maths) / 3
            print("Average:", Average)
        except ValueError:
            print("Please Enter Right Value")  
            continue

        studentdata = {
            "Name": name,
            "Class": Class,
            "Roll No.": RollNumber,
            "Marks in physics:": Physics,
            "Marks in Chemistry:": Chemistry,
            "Marks in Maths:": Maths,
            "Average:": Average
        }

        print(studentdata)

        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(studentdata)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    elif UserChoice == 2:
        search_name = input("Enter Student Name: ")

        try:
            with open("data.json", "r") as f:
                viewdata = json.load(f)

            found = False
            for student in viewdata:
                if student.get("Name", "").lower() == search_name.lower():
                    print("\nStudent Found\n")
                    for key, value in student.items():
                        print(f"{key}: {value}")
                    found = True
                    break
            if not found:
                print("Student Not Found")
        except FileNotFoundError:
            print("data.json not found")
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON. Maybe file is empty or corrupted")
    elif UserChoice == 3:
        search_name = input("Enter Student Name: ")

        with open("data.json", "r") as f:
            viewdata = json.load(f)

        print('''
        Which field do you want to update?
        1 = Name
        2 = Class
        3 = Roll No.
        4 = Marks in physics
        5 = Marks in Chemistry
        6 = Marks in Maths
        ''')

        found = False
        for studentdata in viewdata:
            if search_name.lower() == studentdata.get("Name", "").lower():
                UserUpdate = int(input("Enter The Field Number to Change: "))

                if UserUpdate == 1:
                    studentdata["Name"] = input("Enter New Name: ")
                elif UserUpdate == 2:
                    studentdata["Class"] = input("Enter New Class: ")
                elif UserUpdate == 3:
                    studentdata["Roll No."] = int(input("Enter New RollNumber: "))
                elif UserUpdate == 4:
                    studentdata["Marks in physics:"] = int(input("Enter New Physics Marks: "))
                elif UserUpdate == 5:
                    studentdata["Marks in Chemistry:"] = int(input("Enter New Chemistry Marks: "))
                elif UserUpdate == 6:
                    studentdata["Marks in Maths:"] = int(input("Enter New Maths Marks: "))
                else:
                    print("Enter Valid Field Number")
                    break

                # Recalculate average if marks were changed
                if UserUpdate in [4, 5, 6]:
                    studentdata["Average:"] = (
                        studentdata["Marks in physics:"]
                        + studentdata["Marks in Chemistry:"]
                        + studentdata["Marks in Maths:"]
                    ) / 3

                found = True
                break

        if not found:
            print("Student Not Found")

        else:
            with open("data.json", "w") as f:
                json.dump(viewdata, f, indent=4)


    elif UserChoice == 4:
        try:
            with open("data.json", "r") as f:
                viewdata = json.load(f)
        except FileNotFoundError:
            print("data.json not found")
            continue
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON")
            continue

        print("\nList of Students:")
        for studentdata in viewdata:
            print("-", studentdata.get("Name"))

    else:
        print("Invalid Option. Try Again.")
