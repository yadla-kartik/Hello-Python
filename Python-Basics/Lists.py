#  ---------------- List in Python ----------------

myList = [1,2,3,4,True,1.5,"Hello"]

print(myList[0]) # Accessing the first element of the list

myList[0] = 10 # Modifying the first element of the list
print(myList[0])

# -------------- List Slicing --------------

print(myList[0:3])
print(myList[0:])
print(myList[:4])
print(myList[0:len(myList)])

# -------------- List Traversal --------------

# Using index
for i in range(len(myList)):
    print(myList[i])


# Without using index
for i in myList:
    print(i)


# -------------- List Methods --------------

myList.append("World") # Adding an element to the end of the list
print(myList)
myList.insert(0,0) # Adding an element at a specific index
print(myList)
myList.remove(0) # Removing an element from the list
print(myList)
myList.pop() # Removing the last element from the list
print(myList)
myList.pop(0) # Removing an element at a specific index
print(myList)
myList.clear() # Removing all the elements from the list
print(myList)
