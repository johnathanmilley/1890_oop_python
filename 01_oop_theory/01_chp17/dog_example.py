class Dog:
    """ A basic representation of a dog.

    attributes: self, name, breed, age
    """
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print("ruff ruff")

    def __str__(self):
        return f"{self.name}, {self.breed}, {self.age}"
        #return self.name + ", " + self.breed + ", " + str(self.age)


rusty = Dog("Rusty", "Beagle", "2")

# Overide __str__ in Dog class to print human-readable object info
print(rusty)

# Using dot notation to call an object method
rusty.bark()

# https://www.python.org/dev/peps/pep-0257/
print(rusty.__doc__)