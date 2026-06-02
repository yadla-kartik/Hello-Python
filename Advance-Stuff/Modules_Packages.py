# ----------- Modules and Packages in Python -----------

# A module is a file containing Python definitions and statements. A package is a collection of modules.

# ---- Example of a module: -------

import My_module  # My_module is the name of the module that we want to import. The module should be in the same directory.

from My_module import add  # We can also import specific functions from the module using the from keyword. This allows us to use the function directly without the need to prefix it with the module name.

print(My_module.add(5, 10))  # We can access the functions defined in the module using the dot notation. The add function is defined in the My_module module, and we can call it using My_module.add().
print(My_module.subtract(10, 5))
print(My_module.multiply(5, 10))


# ----- Example of a package: -------

# A package is a collection of modules. It is a way to organize related modules together. A package is a directory.

from Packages import Hello  # Packages is the name of the package that we want to import. The package should be in the same directory.
from Packages import Greet

Hello.hello()  # We can access the functions defined in the module using the dot notation. The hello function is defined in the Hello module, and we can call it using Hello.hello().
Hello.bye()

Greet.greet("Alice")  # The greet function is defined in the Greet module, and we can call it using Greet.greet(). We can also pass an argument to the function, which will be used in the function definition. In this case, we are passing the string "Alice" as an argument to the greet function, which will print a greeting message with the name "Alice".

