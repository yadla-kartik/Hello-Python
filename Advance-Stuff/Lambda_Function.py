# ----- Lambda Functions -----

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is often used for short, simple functions that are not worth defining with a full function definition.

# Example of a lambda function that adds two numbers:

add = lambda x,y : x+y  # The lambda function takes two arguments x and y, and returns their sum. The lambda function is assigned to the variable add, which can be used to call the function. The variable add is a object.

print(add(5,10))

# Lambda functions can also be used with higher-order functions like map(), filter(), and reduce().

# Example of using a lambda function with the map() function to square a list of numbers:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # The map() function takes a function and an iterable as arguments, and applies the function to each item in the iterable. The lambda function is used to square each number in the list. The result is a map object, which is converted to a list using the list() function.

print(squared)

# Example of using a lambda function with the filter() function to filter out even numbers from a list:

even_numbers = list(filter(lambda x: x%2 == 0, numbers))  # The filter() function takes a function and an iterable as arguments, and returns an iterator that contains only the items from the iterable for which the function returns True. The lambda function is used to check if each number in the list is even. The result is a filter object, which is converted to a list using the list() function.

print(even_numbers)

# zip in python is a built-in function that takes two or more iterables (like lists, tuples, etc.) and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables. The zip() function is often used to combine two or more lists into a single list of tuples.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))  # The zip() function takes the two lists as arguments and returns an iterator of tuples. The result is a zip object, which is converted to a list using the list() function.

print(zipped)


