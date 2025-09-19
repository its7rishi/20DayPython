# Variable declaration
# No command for declaration
# Variable is created when value is assigned to it
""" 
x = 5
y = 'Rishi'
print(x)
print(y) 
"""

# Type Casting
# Type of variable can be specified
""" 
x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))
 """

# Single / Double Quotes

"Hello World!"
# Is same as
'Hello World!'

# Case-Sensitive: Variables are case sensitive
""" 
a = 4
# is a different variable
A = 'Mickey'

print(a)
print(A)
 """

# Variable Names
""" 
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
=- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.
 """

# Legal Variable Names
""" 
myvar = "Adam"
my_var = "Adam"
_my_var = "Adam"
muVar = "Adam"
MYVAR = "Adam"
myvar2 = "Adam"
 """

# Illegal Variable Names
""" 
2myvar = "John"
my-var = "Peter"
my var = "Robert"
 """

# Multi Words Variable Names
# Use one of the below styles to make them more readable
""" 
# Camel Case
myFirstVariable = "apple"

# Pascal Case
MySecondVariable = "banana"

# Snake Case
my_third_variable = "cherry"

 """

# Assign Multiple Values
# You can assign values to multiple variables in one line
""" 
x, y, z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)
 """

# One value can be assigned to multiple variables in one line
""" 
a = b = c = "pineapple"
print(a)
print(b)
print(c)
 """

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)