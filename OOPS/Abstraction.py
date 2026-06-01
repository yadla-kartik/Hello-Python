# ------- Abstraction in Python -------

# Abstraction is the process of hiding the internal details of a class and only exposing the necessary information to the outside world. In Python, we can achieve abstraction by using abstract classes and abstract methods.

from abc import ABC, abstractmethod

class Factory(ABC): # Factory class is an abstract class because it inherits from the ABC class which is a built-in class in Python that stands for Abstract Base Class. An abstract class cannot be instantiated and it can only be inherited by other classes.

    @abstractmethod # this is a decorator that is used to declare an abstract method. An abstract method is a method that is declared in the abstract class but does not have any implementation. It is meant to be overridden by the subclasses of the abstract class.
    def display(self):
        pass # this is a placeholder for the implementation of the display method which will be provided by the subclasses of the Factory class.

class CarFactory(Factory): # CarFactory class is a subclass of the Factory class and it provides the implementation of the display method which is declared as an abstract method in the Factory class.
    def display(self):
        print("This is a Car Factory")

class BikeFactory(Factory): # BikeFactory class is a subclass of the Factory class and it provides the implementation of the display method which is declared as an abstract method in the Factory class.
    def display(self):
        print("This is a Bike Factory")

obj1 = CarFactory() # creating an object of the CarFactory class which is a subclass of the Factory class. This shows that we cannot create an object of the abstract class Factory because it is an abstract class and cannot be instantiated.
obj1.display() 

# In the above example, we have created an abstract class Factory which has an abstract method display. We have then created two subclasses CarFactory and BikeFactory which inherit from the Factory class and provide the implementation of the display method. We can create objects of the CarFactory and BikeFactory classes and call the display method which will show the specific implementation of the display method for each subclass. This is how abstraction works in Python by hiding the internal details of the class and only exposing the necessary information to the outside world through abstract methods. 

# If we try to create an object of the abstract class Factory, it will give an error because we cannot instantiate an abstract class. We can only create objects of the subclasses that provide the implementation of the abstract methods declared in the abstract class.

