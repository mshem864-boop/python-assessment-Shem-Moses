"""
task6_oop.py

Name: Shem Moses
Registration No: T006/303998/2024
Institution: The Cooperative University of Kenya (CUK)

Task 6: Object-Oriented Python
"""


class Animal:
    """A simple Animal class demonstrating core OOP concepts."""

    species = "Unknown"   # a. class variable shared by all instances
    counter = 0           # d. tracks total number of instances created

    def __init__(self, name, sound, age):
        self.name = name
        self.sound = sound
        self.__age = age            # f. private attribute (encapsulation)
        Animal.counter += 1         # increase the shared counter

    def speak(self):
        """b. Print the animal's name and its sound."""
        print(f"{self.name} says {self.sound}")

    # f. getter and setter for the private __age attribute
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative.")


class Dog(Animal):
    """e. Dog subclass that extends Animal and overrides speak()."""

    species = "Dog"

    def speak(self):
        print(f"{self.name} barks: {self.sound}!")


if __name__ == "__main__":
    # c. create at least two instances and call speak() on each
    cat = Animal("Whiskers", "Meow", 2)
    cow = Animal("Bella", "Moo", 4)
    cat.speak()
    cow.speak()

    # e. inheritance in action
    dog = Dog("Rex", "Woof", 3)
    dog.speak()

    # d. class variable tracking instance count
    print("Total animals created:", Animal.counter)

    # f. encapsulation: access private __age via getter/setter
    print("Rex's age:", dog.get_age())
    dog.set_age(4)
    print("Rex's age after birthday:", dog.get_age())
