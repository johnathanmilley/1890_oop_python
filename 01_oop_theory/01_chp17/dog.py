class Dog:
    """ docstring goes here

    attributes: name, breed, age
    """
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("ruff ruff")

    def __str__(self):
        #return f"{self.name}, {self.age}"
        return "Name: " + self.name + "Age: " + str(self.age)
    
rusty = Dog("Rusty", "Beagle", 2)
fido = Dog("fido", "Beagle", 2)
buster = Dog("buster", "Beagle", 2)
emma = Dog("emma", "Beagle", 2)
george = Dog("george", "Beagle", 2)

emma.bark()

