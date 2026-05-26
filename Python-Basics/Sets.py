# ------------ Sets ------------

a = {1,1,1,1,8,2,'car',3,4,5,'hello'}

print(a)
print(type(a))

# Sets are unordered, unindexed, and do not allow duplicate values.

# set values are hashed, so they cannot be unordered but you can add new items to a set.

# Sets are mutable, but the items in a set must be immutable. Like strings, numbers, and tuples can be elements of a set, but lists and dictionaries cannot.

# -------- Set Methods --------

# add() method adds an element to the set
a.add('world')
print(a)
a.pop() # removes a random element from the set
print(a)
a.remove(8) # removes the specified element from the set
print(a)
# clear() method removes all the elements from the set
a.clear()
print(a)


# Set operations
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

# Union of sets
print(x | y) # using the | operator
print(x.union(y)) # using the union() method

# Intersection of sets
print(x & y) # using the & operator
print(x.intersection(y)) # using the intersection() method

# Difference of sets
print(x - y) # using the - operator
print(y-x) # using the - operator
print(x.difference(y)) # using the difference() method

# Symmetric difference of sets
print(x ^ y) # using the ^ operator
print(x.symmetric_difference(y)) # using the symmetric_difference() method
