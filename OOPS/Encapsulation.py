# ------- Encapsulation In Python -------

class Factory:
    a = 10 # class attribute

    def show(self): # method
        print(f"This is a Factory class with attribute a = {self.a}")

obj = Factory()

obj.show()
obj.a = 20 # modifying the class attribute a using the object of the class Factory
obj.show() # this will show the modified value of a which is 20, So there is no secuirity in this case because we can modify the class attribute using the object of the class. 

# This is where encapsulation comes into play. Encapsulation is the process of hiding the internal details of a class and only exposing the necessary information to the outside world. In Python, we can achieve encapsulation by using private attributes and methods.

# --------- Access Modifiers in Python ------

class Factory2:
    def __init__(self, private, public, protected):
        self.__private = private # private attribute - only accessible within the class and cannot be accessed from outside the class. It is denoted by double underscore __ before the attribute name.
        self._protected = protected # protected attribute - accessible within the class and its subclasses but not from outside the class. It is denoted by a single underscore _ before the attribute name.
        self.public = public # public attribute - accessible from anywhere, both inside and outside the class. It does not have any special notation.

    def display(self):
        print(f"Factory Name: {self.__private}")
        print(f"Factory Location: {self._protected}")

obj2 = Factory2("Private Factory", "Protected Location", "This is a public attribute")
obj2.display()

obj2._protected = "Modified Protected Location" # we can modify the protected attribute using the object of the class Factory2 because it is accessible within the class and its subclasses but not from outside the class.
print(obj2._protected) # this will show the modified value of the protected attribute which is "Modified Protected Location"

# We cannot access the private attribute directly using the object of the class Factory2 because it is only accessible within the class and cannot be accessed from outside the class. If we try to access the private attribute directly, it will give an error. However, we can access the private attribute using a public method of the class Factory2 which is called getter method.

# So Access modifiers in Python help to achieve encapsulation by controlling the access to the attributes and methods of a class. 