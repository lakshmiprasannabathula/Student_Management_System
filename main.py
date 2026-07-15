
students=[]

def add_student():
    s={}
    s["id"]=input("Enter ID: ")
    s["name"]=input("Enter Name: ")
    s["age"]=input("Enter Age: ")
    s["course"]=input("Enter Course: ")
    students.append(s)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return
    for s in students:
        print("-"*30)
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")

def search_student():
    sid=input("Enter ID: ")
    for s in students:
        if s["id"]==sid:
            print(s)
            return
    print("Student not found.")

def update_student():
    sid=input("Enter ID: ")
    for s in students:
        if s["id"]==sid:
            s["name"]=input("New Name: ")
            s["age"]=input("New Age: ")
            s["course"]=input("New Course: ")
            print("Updated successfully!")
            return
    print("Student not found.")

def delete_student():
    sid=input("Enter ID: ")
    for s in students:
        if s["id"]==sid:
            students.remove(s)
            print("Deleted successfully!")
            return
    print("Student not found.")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=input("Enter choice: ")
    if choice=="1": add_student()
    elif choice=="2": view_students()
    elif choice=="3": search_student()
    elif choice=="4": update_student()
    elif choice=="5": delete_student()
    elif choice=="6":
        break
    else:
        print("Invalid choice.")
