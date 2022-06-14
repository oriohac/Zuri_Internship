
import datetime
import platform


#1
def function( country = "Nigeria" ):
     result = print("I'm from "+country)
     return result
function()
function("Sweden")
function("Antigua and Babuda")


#2
x = lambda a,b : a * b
print(x(10, 11))


#3
def myfunc(n):
      return lambda a : a + n

mydoubler = myfunc(2)

print(mydoubler(11))


#4
#classes
class Person:
      def __init__(self, name, age):
       self.name = name
       self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#5
v = platform.system()
print(v)

#6
y = dir(platform)
print(y)

#7

z = datetime.datetime.now()
print(z.year)
print(z.strftime("%A"))
