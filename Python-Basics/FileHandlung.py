# --------- File Handling in Python ------------------

# To create a file and write some data into it we can use the open() function with 'w' mode.

with open('Python-Basics/example.txt', 'w') as fs:
    fs.write("Hello, this is a file handling example in Python.\n")
    fs.write("We can write multiple lines to the file.\n")
    fs.write("This is the third line.")

# To read the contents of the file we can use the open() function with 'r' mode.

with open('Python-Basics/example.txt', 'r') as fs:
    content = fs.read()
    print(content)

# To append data to the existing file we can use the open() function with 'a' mode.

with open('Python-Basics/example.txt', 'a') as fs:
    fs.write("\nThis line is appended to the file.")

# To read the contents of the file again to see the appended line.
with open('Python-Basics/example.txt', 'r') as fs:
    content = fs.read()
    print(content)

