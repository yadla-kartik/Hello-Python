# -------------- Dictionaries in Python ------------------

a = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(type(a))
print(a['name'])

a['age'] = 31 # update the value of age
print(a)
a['country'] = 'USA' # add a new key-value pair to the dictionary
print(a)
del a['city'] # remove the key-value pair with key 'city'
print(a)

# Dictionaries are ordered, changeable, and indexed. They do not allow duplicate keys.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Key cant be duplicated but values can be duplicated. 

# --------- Traversing a dictionary ---------

for key in a:
    print(key, ":", a[key])

# ---------- Dictionary Methods ---------

# get() method returns the value of the specified key
print(a.get('name'))
# items() method returns a view object that displays a list of dictionary's key-value tuple pairs
print(a.items())
# keys() method returns a view object that displays a list of all the keys in the dictionary
print(a.keys())
# values() method returns a view object that displays a list of all the values in the dictionary
print(a.values())
# pop() method removes the specified key and returns the corresponding value
print(a.pop('age'))
print(a)
# update() method updates the dictionary with the specified key-value pairs
a.update({'age': 31, 'city': 'New York'})
print(a)
# clear() method removes all the elements from the dictionary
a.clear()
print(a)

# Dictionary some operations
x = {'a': 1, 'b': 2, 'c': 3}
y = {'b': 4, 'c': 5, 'd': 6}

# Merging two dictionaries
z = {**x, **y} # using the unpacking operator
print(z)

#  Merging two dictionaries using the update() method
x.update(y)

# Merging two dictionaries using a for loop
for i in y:
    x[i] = y[i]

print(x)