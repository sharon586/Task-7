#Task 2: Apply Abstraction
from abc import ABC, abstractmethod

# Abstract Base Class
class AbstractUser(ABC):
    
    @abstractmethod
    def get_details(self):
        pass


# Parent Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


# Child Class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# Child Class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"


# Child Class: TempFaculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# Testing
users = [
    Student("Shiny", 101, "CSE", 50000),
    Faculty("Ravi", 201, 60000),
    TempFaculty("Anil", 301, 40000, "6 months")
]

for u in users:
    print(u.get_details())