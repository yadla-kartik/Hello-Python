# ------------- Tuples -------------

mytuple = (1,2,3,4,5,True,1.5,"Hello")

print(mytuple[0]) # Accessing the first element of the tuple
# mytuple[0] = 10 # Modifying the first element of the tuple will give an error

# -------------- Tuple Slicing --------------
print(mytuple[0:3])
print(mytuple[0:])
print(mytuple[:4])
print(mytuple[0:len(mytuple)])


# -------------- Tuple Traversal --------------

# Using index
for i in range(len(mytuple)):
    print(mytuple[i])

# Without using index
for i in mytuple:
    print(i)

# -------------- Tuple Methods --------------

# Tuples have only two methods count() and index()
print(mytuple.count(1)) # Count the number of occurrences of an element in the tuple
print(mytuple.index(1.5)) # Return the index of the first occurrence of an element in the tuple