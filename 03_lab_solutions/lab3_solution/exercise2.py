class Person:
    """Representation of a Person

    attributes: first_name, last_name
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'---Person object---\n'
                f'Name: {self.first_name} {self.last_name}')

class Employee(Person):
    """Representation of an Employee (inherits from Person)

    attributes: first_name, last_name, employee_number, position, salary
    """
    def __init__(self, first_name, last_name, 
                employee_number, position, salary):
        super().__init__(first_name, last_name)
        self.employee_number = employee_number
        self.position = position
        self.salary = salary

    def __str__(self):
        return (f'---Employee object---\n'
                f'Name: {self.first_name} {self.last_name}\n'
                f'Employee Number: {self.employee_number}\n'
                f'Position: {self.position}\n'
                f'Salary: ${self.salary}')

    # modifiers 
    def raise_amt(self, amt):
        self.salary += amt

    def change_position(self, new_position):
        self.position = new_position


class Student(Person): 
    """Representation of a Student (inherits from Person)

    attributes: first_name, last_name, student_number, current_courses
    """
    def __init__(self, first_name, last_name, student_number, current_courses):
        super().__init__(first_name, last_name)
        self.student_number = student_number
        self.current_courses = current_courses

    def __str__(self):
        return (f'---Student object---\n'
                f'Name: {self.first_name} {self.last_name}\n'
                f'Student Number: {self.student_number}\n'
                f'Courses: {self.current_courses}')

    def drop_course(self, course):
        self.current_courses.remove(course)

    def add_course(self, course):
        self.current_courses.append(course)


p1 = Person("Adrianne", "Lenker")
p2 = Person("Buck", "Meek")

# print(p1)
# print(p2)

e1 = Employee("John", "Smith", 12345, "Manager", 60000)
e2 = Employee("Marge", "Simpson", 14245, "Realtor", 85000)

# print(e1)
e1.change_position("Regional Manger")
e1.raise_amt(15000)
# print(e1)
# print(e2)

s1 = Student("Mark", "Nobody", 200112442, ['math', 'english', 'gym', 'chemistry'])
s2 = Student("Trish", "Noone", 234325223, ['coding', 'geography', 'gym', 'english'])

print(s1)
s1.drop_course('gym')
s1.add_course('religion')
print(s1)
# print(s2)
