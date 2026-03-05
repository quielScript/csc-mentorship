# OOP - Object Oriented Programming
# POOP - Python Object Oriented Programming
# Attributes - kung unsay naa sa class (name, id, age, address, etc.) -> describe
# Behaviors - functionalities (functions)

class Person:
    # self = person_1
    def __init__(self, name, age, address):
        # Attributes
        self.name = name
        self.age = age
        self.address = address

    # Behaviors/method
    def greet(self, greeting):
        print(f"{greeting}! I am {self.name}")

# Object
person_1 = Person("Justin", 23, "Nabunturan")

# Accessing attributes (object.attribute-name)
print(person_1.name)
print(person_1.age)
print(person_1.address)

# Accessing functions
person_1.greet("Wassup")

# Encapsulation (lock/secure/private data)
class Person:
    def __init__(self, name, age, contactNum):
        self.__name = name
        self.age = age
        # Private attribute
        # self.__contactNum = contactNum
        self.contactNum = contactNum

    # Setter method
    def setName(self, name):
        self.__name = name

    # Getter method - get any attribute or data from the class
    # def displayContactNum(self):
    #     print(self.__contactNum)

    def displayContactNum(self):
        print(self.contactNum)

    def displayName(self):
        print(self.__name)

person_1 = Person("Justin", 3, 921323244)

# print(person_1.name)
# print(person_1.age)
# print(person_1.contactNum)
# person_1.displayContactNum()

# Changing value of an attribute
person_1.displayName()
person_1.setName("JM")
person_1.displayName()

# Inheritance
# Parent class
class Vehicle:
    def __init__(self, type):
        self.type = type

    def showVehicleType(self):
        print(f"This vehicle is a {self.type}")

# Child class
class Car(Vehicle):
    def __init__(self, model, year, color):
        super().__init__("Car")
        # Attributes
        self.model = model
        self.year = year
        self.color = color

    # Methods
    def drive(self):
        print("Brooooooom!!!")

    def stop(self):
        print("Stopped")

class Motorcycle(Vehicle):
    def __init__(self,  color, model = "Kawasaki H2", year = 2025, numWheels = 2):
        super().__init__("Motorcycle")
        self.model = model
        self.year = year
        self.color = color
        self.numWheels = numWheels


# Object/instance
car_1 = Car("Toyota", 2025, "red")
motor = Motorcycle("green")

# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# car_1.drive()

print(motor.numWheels)

# Abstraction - hiding the logic

from add import addNums

addNums(2, 3)

# Multiple inheritance
class Mom:
    def __init__(self):
        self.isWhite = True
        self.isKind = False
        self.isHardworking =True

class Dad:
    def __init__(self):
        self.isTall = True
        self.isAGoodCook = True

class Child(Mom, Dad):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Neighbor(Child):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

child_1 = Child("Justin")
print("This kid is kind" if child_1.isKind else "This kid is not kind")

n_1 = Neighbor("Justin")
print(n_1.isKind)

# Polymorphism
class Person:
    def __init__(self, name, age):
        # self = person_1
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}!")


class BisayaPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    # Polymorph
    def greet(self):
        print(f"Madayaw {self.name}! Taga asa deay ka?")

bisakol = BisayaPerson("Justin", 23)
person_1 = Person("Jasper", 23)
person_2 = Person("JM", 23)
person_3 = Person("Prince", 23)
bisakol.greet()
# person.greet()