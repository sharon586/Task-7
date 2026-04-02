# Task 5: Use filter()
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


# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))


print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)