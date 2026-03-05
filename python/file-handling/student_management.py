import os

class Student:
    def __init__(self, name, student_id, age, grade):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grade = grade

    # Dunder method
    def __str__(self):
        return f"Name: {self.name},ID: {self.student_id}, Age: {self.age}, Grade: {self.grade}"

    def to_file_format(self):
        return f"{self.name},{self.student_id},{self.age},{self.grade}"

    @classmethod
    def from_file_format(cls, line):
        name, student_id, age, grade = line.strip().split(",")
        return cls(name, student_id, age, grade)

class StudentManagementSystem:
    def __init__(self, filename = "students.txt"):
        self.filename = filename
        self.students = self.load_students_from_file()

    def load_students_from_file(self):
        students = []
        if os.path.exists(self.filename):
            with open (self.filename, "r") as file:
                for line in file:
                    students.append(Student.from_file_format(line))
        return students

    def save_students_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(student.to_file_format() + "\n")

    def add_student(self, student):
        self.students.append(student)
        self.save_students_to_file()

    def view_students(self):
        if not self.students:
            print("No records found!")
            return

        for student in self.students:
            print(student)

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student)
                return

        print(f"Student with {student_id} not found!")

    def update_student(self, student_id, updated_student):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                self.students[i] = updated_student
                self.save_students_to_file()
                print("Student updated!")
                return

        print(f"Student with {student_id} not found!")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                self.save_students_to_file()
                print("Student deleted!")
                return

        print(f"Student with {student_id} not found!")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student by ID")
        print("5. Delete Student by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            student = Student(name, student_id, int(age), grade)
            sms.add_student(student)
        elif choice == '2':
            sms.view_students()

        elif choice == '3':
            student_id = input("Enter student ID to search: ")
            sms.search_student_by_id(student_id)

        elif choice == '4':
            student_id = input("Enter student ID to update: ")
            new_name = input("Enter new student name: ")
            age = input("Enter new student age: ")
            grade = input("Enter new student grade: ")
            updated_student = Student(new_name, student_id, age, grade)
            sms.update_student(student_id, updated_student)

        elif choice == '5':
            student_id = input("Enter student ID to delete: ")
            sms.delete_student(student_id)

        elif choice == '6':
            print("Bye bye!")
            break

        else:
            print("Invalid choice!")

main()


