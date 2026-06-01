#  ---------- Class and Objects in python ----------

class Factory:
    a = 12 # attributes

    def display(self): # method
        print("This is a Factory class")
    
    print("This is a Factory class and this will only print one time at the time of instantiation") 


# Directly accessing the attribute and methods using class name
print(Factory.a) # accessing the attribute a using class name
Factory().display() # accessing the method display() using class name and passing the object as an argument


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

# --------------- Types of Methods in python ---------------

# -- 1. Instance Methods --

class Factory3:
    def instance_method(self): # instance method. the self represents the instance of the class and is used to access instance attributes and methods
        print("This is an instance method")

obj4 = Factory3()
obj4.instance_method() 

# -- 2. Static Methods --

class Factory4:
    @staticmethod  #it is a decorator to define a static method
    def static_method(): # static method
        print("This is a static method")

obj = Factory4() 
obj.static_method()

# -- 3. Class Methods --

class Factory5:
    @classmethod # it is a decorator to define a class method
    def class_method(cls): # class method. cls represents the class itself and is used to access class attributes and methods
        print("This is a class method")

obj5 = Factory5()
obj5.class_method()