   # Class & Object

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p = Person("Alice")
p.greet()



  # Inheritance

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()




   # Polymorphism

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

animals = [Cat(), Dog()]
for a in animals:
    a.speak()  # Different output, same method name
