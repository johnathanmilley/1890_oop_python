# Lab 2 Q1 Solution

class Dog:
    """ docstring goes here """
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

def sameDog(dog1, dog2):
    """ A test of deep equality between 2 Dog objects """
    return (dog1.name == dog2.name
            and dog1.breed == dog2.breed
            and dog1.age == dog2.age)

sam = Dog("Sam", "German Spitz", 15)
sammy = Dog("Sam", "German Spitz", 15)
samuel = sam
baily = Dog("Baily", "Pointer", 9)

# Test shallow equality
print(sam == sammy)     # False
print(sam == samuel)    # True - they point to the same object in memory

# Test deep equality
print(sameDog(sam, sammy)) # True - the instance variables in each object are equal
print(sameDog(sam, baily)) # False



