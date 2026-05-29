from pathlib import Path
import os

def readfileAndfolder():
    path = Path('./Projects')
    items = list(path.glob('*'))
    for i, item in enumerate(items):
        print(f"{i+1}. {item.name}")

def createfile():
    try:
        readfileAndfolder()

        fileName = input("Enter the name of the file you want to create (with extension) :- ")
        p = Path("./Projects/" + fileName)
        if p.exists() and p.is_file():
            print(f"{fileName}File already exists.")
        else: 
            with open(p, 'w') as fs:
                data = input("Enter the data you want to write in the file :- ")
                fs.write(data)
            print('FILE CREATED SUCCESSFULLY')
        
        
    except Exception as err:
        print(f"An error occurred: {err}")
    
    
def readfile():
    try:
        readfileAndfolder()

        fileName = input("Enter the name of the file you want to read (with extension) :- ")
        p = Path("./Projects/" + fileName)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(f"Data in {fileName} is :- \n{data}")
            print('FILE READ SUCCESSFULLY')
        else: 
            print(f"{fileName}File does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")


def updatefile():
    try:
        readfileAndfolder()

        fileName = input("Enter the name of the file you want to update (with extension) :- ")
        p = Path("./Projects/" + fileName)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")
            check = int(input("Enter your response :- "))
            if check == 1:
                newName = input("Enter the new name of the file (with extension) :- ")
                p.rename("./Projects/" + newName)
                print('FILE NAME CHANGED SUCCESSFULLY')
            elif check == 2:    
                with open(p, 'w') as fs:
                    data = input("Enter the data you want to write in the file :- ")
                    fs.write(data)
                print('FILE UPDATED SUCCESSFULLY')
            elif check == 3:
                with open(p, 'a') as fs:
                    data = input("Enter the data you want to append in the file :- ")
                    fs.write(" " + data)
                print('FILE UPDATED SUCCESSFULLY')
        else: 
            print(f"{fileName}File does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")

def deletefile():
    try:
        readfileAndfolder()

        fileName = input("Enter the name of the file you want to delete (with extension) :- ")
        p = Path("./Projects/" + fileName)
        if p.exists() and p.is_file():
            os.remove(p)
            print('FILE DELETED SUCCESSFULLY')
        else: 
            print(f"{fileName}File does not exist.")

    except Exception as err:
        print(f"An error occurred: {err}")

print("Welcome to the File Handling Project")

print ("1. Create a new file")
print ("2. Read a file")
print ("3. Update a file")
print ("4. Delete a file")

check = int(input("Enter your response :- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()