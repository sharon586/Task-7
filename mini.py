#Final Challenge (Important 🔥)
#Build a mini system:

from abc import ABC, abstractmethod
from functools import reduce

# ------------------ ABSTRACTION ------------------
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ------------------ BASE CLASS ------------------
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


# ------------------ CHILD CLASSES ------------------
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> {self.name}, ID: {self.id}, Salary: {self.salary}"


# ------------------ DATA ------------------
students = [
    Student("Shiny", 101, "CSE", 50000),
    Student("Ravi", 102, "ECE", 40000),
    Student("Anil", 103, "IT", 60000)
]

faculty = [
    Faculty("Kiran", 201, 25000),
    Faculty("Meena", 202, 50000),
    Faculty("Raj", 203, 35000)
]


# ------------------ HIGHER ORDER FUNCTION ------------------
def process_users(users, func):
    return list(map(func, users))


# ------------------ 1. PRINT ALL DETAILS ------------------
print("---- ALL DETAILS ----")
for u in students + faculty:
    print(u.get_details())


# ------------------ 2. SORTING ------------------
print("\n---- SORTED DATA ----")

sorted_students = sorted(students, key=lambda s: s.fees)
sorted_faculty = sorted(faculty, key=lambda f: f.salary)

print("Students by Fees:")
for s in sorted_students:
    print(s.name, s.fees)

print("\nFaculty by Salary:")
for f in sorted_faculty:
    print(f.name, f.salary)


# ------------------ 3. FILTERING ------------------
print("\n---- FILTERED DATA ----")

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)


# ------------------ 4. MAP (TRANSFORM) ------------------
print("\n---- STUDENT NAMES (MAP) ----")
names = process_users(students, lambda s: s.name)
print(names)


# ------------------ 5. REDUCE (AGGREGATE) ------------------
print("\n---- TOTALS ----")

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees:", total_fees)
print("Total Salary:", total_salary)


# ------------------ 6. COMBINED FUNCTIONAL PIPELINE ------------------
print("\n---- COMBINED (FILTER + MAP + SUM) ----")

# Total fees of students with fees > 50000
total_high_fee = sum(
    map(lambda s: s.fees,
        filter(lambda s: s.fees > 50000, students))
)

print("Total Fees ( >50000 ):", total_high_fee)
