# ------------- Constructor in python -------------

# Constructor is a special method in python that is used to initialize the object of a class. It is called when an object of the class is created. The constructor method is defined using the __init__() method.

class Factory:
    def __init__(self, name, location): # constructor method. The init is a special method called Dunder
        self.name = name # instance variable
        self.location = location # instance variable

    def display(self): # method
        print("This is a Factory class")
        print("Factory Name:", self.name)
        print("Factory Location:", self.location)

obj = Factory("ABC Factory", "New York") # creating object of class Factory and passing the arguments to the constructor
obj.display() # calling the display method on the object