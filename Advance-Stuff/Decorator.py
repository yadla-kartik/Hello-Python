# ----------- Decorator in Python -----------

# A decorator is a design pattern in Python that allows you to modify the behavior of a function or class method without changing its source code.

# Example of a simple decorator that adds a greeting before calling the original function:

class Animal:
    @property
    def hello(self):
        print("Hello, World!")

animal = Animal()
animal.hello


#  We can create our own Decorator to modify the behavior of the function:

def my_decorator(func):  # func is a function that we want to decorate here the my_function is passed as an argument to the decorator function. And the my_decorator is called before the my_function is executed.
    def wrapper(): # wrapper is a nested function that will be returned by the decorator. It will be called instead of the original function when we call the decorated function. 
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@my_decorator
def my_function():
    print("This is my function.")

my_function()  # When we call the decorated function, it will execute the wrapper function instead of the original function. The wrapper function will print "Before calling the function.", then call the original function, and finally print "After calling the function."

# -- PASSING PARAMETERS TO THE DECORATOR --

def my_decorator2(func):
    def wrapper(a, b): # WHEN THE ORIGINAL MY_FUNCTION PASSES AN ARGUMENT TO THE DECORATOR THEN THE DECORATOR WILL NOT ACCEPT THAT ARGUMENT. IT WILL GIVE AN ERROR BECAUSE THE DECORATOR IS NOT DESIGNED TO ACCEPT ANY ARGUMENTS. THE WRAPPER FUNCTION IS DESIGNED TO ACCEPT ANY ARGUMENTS. SO IF THE ORIGINAL FUNCTION PASSES AN ARGUMENT TO THE DECORATOR THEN THE WRAPPER FUNCTION WILL ACCEPT THAT ARGUMENT AND PASS IT TO THE ORIGINAL FUNCTION. IF THERE ARE SO MANY ARGUMENTS IN THE ORIGINAL FUNCTION THEN THE WRAPPER FUNCTION CAN ACCEPT ANY NUMBER OF ARGUMENTS USING *args AND **kwargs. THIS IS CALLED VARIADIC FUNCTIONS IN PYTHON. IT ALLOWS US TO PASS ANY NUMBER OF ARGUMENTS TO THE FUNCTION.
        print("Before calling the function.")
        func(a, b)
        print("After calling the function.")
    return wrapper

@my_decorator2
def my_function2(x, y):
    print(f"The sum of {x} and {y} is {x + y}.")

my_function2(5,10)