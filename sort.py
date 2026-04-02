#Task 3: Sorting using key
# Reusing previous classes

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


# Create list of students
students = [
    Student("Shiny", 101, "CSE", 50000),
    Student("Ravi", 102, "ECE", 40000),
    Student("Anil", 103, "IT", 60000)
]

# Sort students by fees
students.sort(key=lambda x: x.fees)

print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)


# Create list of faculty
faculty_list = [
    Faculty("Kiran", 201, 70000),
    Faculty("Meena", 202, 50000),
    Faculty("Raj", 203, 90000)
]

# Sort faculty by salary
faculty_list.sort(key=lambda x: x.salary)

print("\nFaculty sorted by salary:")
for f in faculty_list:
    print(f.name, f.salary)