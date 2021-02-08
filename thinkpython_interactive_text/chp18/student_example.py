class Student:
    """ A basic representation of a student.

    attributes: firstname, lastname, id, program_of_study
    """
    def __init__(self, firstname, lastname, id, program_of_study):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.program_of_study = program_of_study

    
student1 = Student("Angela", "Olson", 14012421, "Software Developer")
student2 = Student("Jeff", "Tweedy", 12401841, "Nursing")

# using dot notation to access object data
print(student2.firstname)
print(student2.id)

print('\n')

# formatted using f-strings (more here: https://www.python.org/dev/peps/pep-0498/)
print(f"{student1.firstname[0]}. {student1.lastname}")

print('\n')

# more on doc strings here: https://www.python.org/dev/peps/pep-0257/
print(student1.__doc__)