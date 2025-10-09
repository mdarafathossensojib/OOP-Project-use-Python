class StudentDatabase:
    __student_list = []  # private list

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_all_students(cls):
        return cls.__student_list

    @classmethod
    def find_student_by_id(cls, student_id):
        for student in cls.__student_list:
            if student.get_id() == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student '{self.__name}' is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student '{self.__name}' has been enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student '{self.__name}' is not currently enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student '{self.__name}' has been dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"\nStudent ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Status: {status}")

    def get_id(self):
        return self.__student_id



Student(1, "Alice", "Computer Science")
Student(2, "Bob", "Physics", True)
Student(3, "Charlie", "Chemistry")

def menu():
    while True:
        print("\n===== STUDENT DATABASE MENU =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            students = StudentDatabase.get_all_students()
            if not students:
                print("No students found.")
            else:
                for s in students:
                    s.view_student_info()

        elif choice == '2':
            try:
                sid = int(input("Enter Student ID to Enroll: "))
                student = StudentDatabase.find_student_by_id(sid)
                if student:
                    student.enroll_student()
                else:
                    print("Invalid Student ID.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == '3':
            try:
                sid = int(input("Enter Student ID to Drop: "))
                student = StudentDatabase.find_student_by_id(sid)
                if student:
                    student.drop_student()
                else:
                    print("Invalid Student ID.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == '4':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice! Please enter 1-4 only.")



menu()

