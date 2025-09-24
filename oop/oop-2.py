class Person:
    # Constructor
    def __init__(self, name, age):
        # Attributes
        # self -> person_1
        self.name = name
        self.age = age

    # Methods (functions)
    def sayHi(self):
        print(f"Hello! I am {self.name}, {self.age} year/s old :)")

person_1 = Person("Clark", 20)

# Accessing/getting attributes
print(person_1.name)
print(person_1.age)

# Calling methods (functions)
person_1.sayHi()

# Inheritance
# Parent -> Person
class Student(Person):
    def __init__(self, name, age, program, student_id):
        # Parent constructor
        super().__init__(name, age)
        # Attributes
        self.program = program
        self.student_id = student_id

    def displayStudentInfo(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Program: {self.program}\n"
              f"Student ID: {self.student_id}")

student_1 = Student("Justin", 23, "BSIT", 2744)
student_2 = Student("Clark", 19, "BSCE", 1111)

student_1.displayStudentInfo()
print("-----------------------")
student_2.displayStudentInfo()

# Accessing methods and attributes from parent class
student_1.sayHi()
print(student_1.name)
