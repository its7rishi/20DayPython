""" MODULES """

# ? Modules are like code libraries
# ? They contain a set of functions that you can include in your application
# ? Modules can also contain variables of all types

# * CREATE A MODULE

# ? To create a module, save the code you want in a file with the extension ' .py '

# * IMPORT A MODULE
""" 
import my_module

my_module.greeting('Rishi') # Output => Hello, Rishi!

print(my_module.person['name']) # Output => Johnny
 """

# * RENAMING A MODULE

# ? You can create a alias when importing a module
# ? use the ' as ' keyword
""" 
import my_module as myMod

myMod.greeting('Kyle') # Output => Hello, Kyle!
 """

# * BUILT IN MODULES

# ? There are many in built modules in Python. They can be imported as needed


# platform module
""" 
import platform

x = platform.system()
print(x) # Output: Darwin

# * dir() Function
# ? It is a built in function to list all variables and methods in a module

y = dir(platform)
print(y)
 """

# * IMPORTING FROM MODULE

# ? You can choose to import only part of the module
# ? use the ' from ' keyword

# ! When importing using the ' from ' keyword do not use th module name when referring to elements in the module

from my_module import(person)

print(person['city']) # Output; Seoul