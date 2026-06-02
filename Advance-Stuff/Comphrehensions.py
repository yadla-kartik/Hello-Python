#  -------------- COMPREHENSIONS IN PYTHON----------------

# Comprehensions are a concise way to create lists, dictionaries, sets, and generators in Python.


# -- List Comprehension --

lists = [i for i in range(1, 11) if i%2 == 0]
print(lists)


# -- Dictionary Comprehension --

dicts = {i: i**2 for i in range(1, 11) if i%2 == 0}
print(dicts)

# -- Set Comprehension --

sets = {i for i in range(1, 11) if i%2 == 0}
print(sets)