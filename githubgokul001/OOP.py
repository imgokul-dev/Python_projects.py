from secrets import choice


class student:
    def __init__(self,name,age,course):
        self.name = name 
        self.age = age
        self.course = course

student = []

def add_student():
    name = input("Enter student name: " )
    age = input("Enter student age: ")
    course = input("Enter the studet's couurse: ")

    student = student(name,age,course)
    students.append(student)

def display_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print("Name:",student.name)
            print("Age:",student.age)
            print("Course:",student.course)
            print("--------------------")
def search_student():
    name = input("Enter student na,e to search: ")

    for student in students:
        if student.name.lower()==name.lower():
            print("Student found!")
            print("Name:",student.name)
            print("Age:",student.age)
            print("Course:",student.course)
            return
    print("Student not found.")


while True:
    print("\n---STUDENT MANAGEMENT SYSTEM---")
    print("1.Add student")
    print("2.Display student")
    print("3.Search student")
    print("4.Display all students")
    print("5.Exit")

    choice == input ("Enter your choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")




            
