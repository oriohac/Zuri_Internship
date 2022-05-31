# class MyClass:
#     def method(self):
#         return 'instance method called', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method called'
# obj = MyClass()
# obj.classmethod()
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'pizza({self.ingredients!r})'
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella','tomatoes','ham'])
# Pizza.margherita()
import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
    def __repr__(self):
        return(f'Pizza({self.radius!r},'f'{self.ingredients!r})')
    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return math.pi*r**2
p = Pizza(4,['mozzarella','tomatoes'])
#p.area()
Pizza.circle_area(4)