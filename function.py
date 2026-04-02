#Task 7: Higher Order Function

# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


# Sample classes
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees


# Data
students = [
    Student("Shiny", 101, "CSE", 50000),
    Student("Ravi", 102, "ECE", 40000),
    Student("Anil", 103, "IT", 60000)
]


# Use case 1: Extract names
names = process_users(students, lambda s: s.name)

# Use case 2: Extract fees
fees = process_users(students, lambda s: s.fees)

print("Names:", names)
print("Fees:", fees)