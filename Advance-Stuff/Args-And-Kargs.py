# ------- Args and Kargs in Python -------

# In Python, *args and **kwargs are used to pass a variable number of arguments to a function.

# *args allows you to pass a variable number of non-keyword arguments to a function. It is represented by an asterisk (*) followed by a variable name. The arguments passed using *args are treated as a tuple inside the function.

def my_function(*args):
    for arg in args:
        print(arg)
    
my_function(1, 2, 3, 4, 5)  

# **kwargs allows you to pass a variable number of keyword arguments to a function. It is represented by two asterisks (**) followed by a variable name. The arguments passed using **kwargs are treated as a dictionary inside the function.

def my_function2(**kwargs):
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

my_function2(name="John", age=30, city="New York")



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        func(*args, **kwargs)
        print("After calling the function.")
    return wrapper

@my_decorator
def my_function3(x, y,e,s,f,g,h):
    sum = x + y + e + s + f + g + h
    print('The sum of the numbers is:', sum)
        

my_function3(5, 10, 1, 2, 3, 4, 5)