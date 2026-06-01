# --------- Inheritance in Python -----------

class Animal: # Animal class is called a parent class or superclass
    def __init__(self, name):
        self.name = name

    def name(self):
        return f"Animal name is {self.name}"

class Dog(Animal):   # Dog class inherits from Animal class and is called a child class or subclass
    def speak(self):
        return "Woof!" 
    
obj = Dog("Buddy") # creating an object of the Dog class and passing the name as an argument to the constructor of the Animal class. This shows that the Dog class can access the attributes and methods of the Animal class because of inheritance.
print(obj.name) # accessing the name attribute of the Animal class using the object of the Dog class
print(obj.speak())

# ---- Super() function in Python ----

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent name is {self.name}")
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # using super() to call the constructor of the Parent class and pass the name argument to it
        self.age = age

    def display2(self):
        super().display() # using super() to call the display method of the Parent class
        print(f"Child age is {self.age}")

obj2 = Child("Alice", 10) # creating an object of the Child class and passing the name and age as arguments to the constructor of the Child class. This shows that the Child class can access the attributes and methods of the Parent class because of inheritance and also can use the super() function to call the constructor and methods of the Parent class.
obj2.display2() # calling the display2 method of the Child class which in turn calls the display method of the Parent class using super()

# ---- Types of Inheritance in Python ----

# -- 1. Single Inheritance --

# In single inheritance, a child class inherits from a single parent class. This we have already seen in the above example where the Dog class inherits from the Animal class.

# -- 2. Multiple Inheritance --

# In multiple inheritance, a child class inherits from multiple parent classes. 

class Parent1:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print("This is method1 from Parent1 class")

class Parent2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method2(self):
        print("This is method2 from Parent2 class")

class Child2(Parent1, Parent2): # Child class inherits from both Parent1 and Parent2 classes
    def __init__(self, name, age):
        Parent1.__init__(self, name)
        Parent2.__init__(self, name, age)

    def method3(self):
        print("This is method3 from Child class")

obj3 = Child2('Alice', 10) # The Child2 class ask for the argument of Parent1 first because it is the first parent class in the inheritance list and then it ask for the argument of Parent2 class. This shoes the MRO (Method Resolution Order) in Python which is the order in which the methods are inherited from the parent classes. In this case, the Child2 class will first look for the method in Parent1 class and then in Parent2 class if it is not found in Parent1 class.

obj3.method1() # accessing method1 from Parent1 class using the object of the Child2 class
obj3.method2() # accessing method2 from Parent2 class using the object of the Child2 class
obj3.method3() # accessing method3 from Child2 class using the object of the Child2 class

# -- 3. Multilevel Inheritance --

class Industry:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalIndustry(Industry):
    def __init__(self, material, zips, color):
        super().__init__(material, zips) # using super() to call the constructor of the Industry class and pass the material and zips arguments to it
        self.color = color

class PuneIndustry(BhopalIndustry):
    def __init__(self, material, zips, color, size):
        super().__init__(material, zips, color) # using super() to call the constructor of the BhopalIndustry class and pass the material, zips and color arguments to it
        self.size = size

obj4 = PuneIndustry("Fiber", "12345", "Red", "Large") # creating an object of the PuneIndustry class and passing the material, zips, color and size as arguments to the constructor of the PuneIndustry class. This shows that the PuneIndustry class can access the attributes and methods of both the BhopalIndustry and Industry classes because of multilevel inheritance.


