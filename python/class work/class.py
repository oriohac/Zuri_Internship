from typing_extensions import Self
from unicodedata import name


class Vehicle():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("my name is ", name, "and i am ", age)
    def speak(self):
        print("this is the speak function",self.name, "and this is the age",self.age)


h = Dog("henry", 70)
print(h.speak)
h.speak()

def addme(self, school):
    self.school = school
    print("this is school", school)

#child class
class Truck(Vehicle):
    def __init__(self, name, fuel):
        self.fuel = 30
        self.name = "Truck"
print("this is the cars name",self.name)

h = Dog("tim", 50)
print(h.addme("school"))