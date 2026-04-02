#Task 6: Use reduce()

from functools import reduce

# Sample classes
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees   # should be int


class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary   # should be int


# Data
students = [
    Student("Shiny", 101, "CSE", 50000),
    Student("Ravi", 102, "ECE", 40000),
    Student("Anil", 103, "IT", 60000)
]

faculty_list = [
    Faculty("Kiran", 201, 25000),
    Faculty("Meena", 202, 50000),
    Faculty("Raj", 203, 35000)
]


# Total fees
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

# Total salary
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)


print("Total Fees:", total_fees)
print("Total Salary:", total_salary)