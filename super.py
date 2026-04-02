#Task 1: Use super() properly
# Parent Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Child Class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


# Child Class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


# Child Class: TempFaculty (inherits from Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


# Testing
s = Student("Shiny", 101, "CSE", 50000)
f = Faculty("Ravi", 201, 60000)
t = TempFaculty("Anil", 301, 40000, "6 months")

print(s.__dict__)
print(f.__dict__)
print(t.__dict__)