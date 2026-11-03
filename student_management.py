class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark


students = []


def add_student():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    mark = float(input("Enter your mark: "))

    student = Student(name, age, mark)
    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student.name, student.age, student.mark)


def calculate_average():
    if len(students) == 0:
        print("No student available.")
        return

    total = 0
    for student in students:
        total += student.mark

    average = total / len(students)
    print("Average marks:", average)


while True:
    print("\n=====STUDENT MANAGEMENT SYSTEM=====")
    print("1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

        







