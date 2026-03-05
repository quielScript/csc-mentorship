import os

class Student:
    def __init__(self, name, id, age, grade):
        self.name = name
        self.id = id
        self.age = age
        self.grade = grade

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Student: {self.id}\n"
                f"Age: {self.age}\n"
                f"Grade: {self.grade}\n")

    def to_file_format(self):
        return f"{self.name}|{self.id}|{self.age}|{self.grade}"

    @classmethod
    def from_file_format(cls, line):
        name, id, age, grade = line.strip().split("|")
        return cls(name, id, age, grade)

class StudentManagementSystem:
    def __init__(self, filename = "students.txt"):
        self.filename = filename
        self.students = self.load_students_from_file()

    def load_students_from_file(self):
        students = []
        if os.path.exists(self.name):
            with open(self.filename, "r") as file:
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
            print("No students found!")
            return

        for student in self.students:
            print(student)

    def search_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                print(student)
                return

        print(f"No student found with ID: {id}")

    def update_student(self, id, new_student):
        for i, student in enumerate(self.students):
            if student.id == id:
                self.students[i] = new_student
                self.save_students_to_file()
                print("Student updated!")
                return

        print(f"No student found with ID: {id}")

    def delete_student(self, id):
        for i, student in enumerate(self.students):
            if student.id == id:
                del student[i]
                self.save_students_to_file()
                print("Student deleted!")
                return
        print(f"No student found with ID: {id}")