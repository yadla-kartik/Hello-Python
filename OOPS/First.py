#  ---------- Class and Objects in python ----------

class Factory:
    a = 12 # attributes

    def display(self): # method
        print("This is a Factory class")
    
    print("This is a Factory class and this will only print one time at the time of instantiation") 


# Directly accessing the attribute and methods using class name
print(Factory.a) # accessing the attribute a using class name
Factory.display(obj) # accessing the method display() using class name and passing the object as an argument


# creating an object of the class
obj = Factory() # object of the class Factory


# accessing the attributes and methods of the class using the object
print(obj.a) # accessing the attribute a
obj.display() # accessing the method display()

# ---------- Types of Attributes in python ----------

# -- 1. Instance Attributes --

class Factory2:
    def __init__(self, name, location): # constructor method. The init is a special method called Dunder
        self.name = name # instance variable
        self.location = location # instance variable

    def display(self): # method
        print("This is a Factory2 class")
        print("Factory2 Name:", self.name)
        print("Factory2 Location:", self.location)

obj3 = Factory2("XYZ Factory", "Los Angeles") # creating an object of the class Factory2 and passing the arguments to the constructor
obj3.display() 

# -- 2. Class Attributes --

class Industry:
    a = 12 # class attribute
    b = "Hello" # class attribute

    def display(self): # method
        print("This is a Industry class")
        print("Value of a:", self.a)
        print("Value of b:", self.b)

obj1 = Industry()
obj1.display()