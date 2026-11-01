students={}
def add_student():
    roll=input("Enter roll:")
    name=input("Enter name:")
    dept=input("Enter department:")
    students[roll]={"name":name,"department":dept}
    print("students added")
    def view_student():
        if not students:
            print("no student records found")
            return
        print("----students record----")
        for roll,data in students.items():
            print("Roll no:",roll,"|Name:",data["name"],"|department:",data["department"])
    def search_student():
        roll=input("enter roll no:")
        if roll in students:
            print(students[roll])
        else:
            print("students not found")
    def delete_students():
        roll=input("enter roll to delete:")
        if  roll in students:
            del students[roll]
            print("student successfully.")
        else:
            print("students not found")
while True:
    print("\n1.add student")
    print("2. view students")
    print("3.search students")
    print("4.delete students")
    print("5.exit")
    choice=input("enter choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_students()
    else:
        print("invaild choice")
        break
        
