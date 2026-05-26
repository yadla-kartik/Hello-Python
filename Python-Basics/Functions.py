#  -------------- Functions --------------

def hello():
    print("Hello Python welcome to functions")

hello()


# Types of Arguments

# -------------- Positional Arguments --------------

def sum(a,b):
    print(f"Sum of a and b is {a+b}")

sum(10,20)


# --------------- Keyword Arguments --------------
def minus(a,b):
    print(f"Difference of a and b is {a-b}")

minus(b=10,a=20)

# -------------- Default Arguments --------------

def multiple(a,b=10):
    print(f'Multiple of a and b is {a*b}')

multiple(5)


# ------------------ variable length arguments --------------
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(f'Sum of all the numbers is {sum}')

add(1,2,3,4,5)

# ------------ Return Statement --------------

def helllo():
    return "Hello Python welcome to functions which have return statement"

print(helllo())