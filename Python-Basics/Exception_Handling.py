# ------------ Exception Handling in Python ------------------

# a = int(input("Enter you no :- "))

# div = 10/a 
# print(div)
# The above code will throw an error if the user enters 0 as input. To handle this we can use try and except block.

try:
    a = int(input("Enter you no :- "))
    div = 10/a 
    print(div)

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("This block will execute only if there is no error in the try block.")

finally:
    print("This block will always execute whether an error occurs or not.")
