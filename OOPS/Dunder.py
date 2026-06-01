# ----- Dunder Methods in Python -----

# Dunder methods are special methods in Python that have double underscores at the beginning and end of their names. They are also known as magic methods or special methods. Dunder methods are used to define the behavior of objects in Python and they are automatically called by Python when certain operations are performed on the objects.

class Factory:
    def __init__(self, name, age): # constructor method. The init is a special method called Dunder
        self.name = name # instance variable
        self.age = age # instance variable

    def __str__(self): # this is a dunder method that is used to define the string representation of the object. It is called when we try to print the object or convert it to a string.
        return f"Factory Name: {self.name} and Age: {self.age}"
    
    def __add__(self, other): # this is a dunder method that is used to define the behavior of the addition operator + when it is used with objects of the Factory class. It takes another object as an argument and returns a new object that is the result of the addition.
        return f"Your are adding {self.age} and {other.age} which is {self.age + other.age}"
    
    
obj = Factory("ABC Factory", 5)
obj2 = Factory("XYZ Factory", 10)

print(obj) # when we try to print the object, it will call the __str__ method of the Factory class and return the string representation of the object which is "Factory Name: ABC Factory and Age: 5" in this case. If we do not define the __str__ method in the Factory class, it will return the default string representation of the object which is something like <__main__.Factory object at 0x7f8b8c8c8c8c>.

print(obj2)
print(obj + obj2)