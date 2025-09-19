# Generic numeric types in Python
""" 
- int
- float
- complex
 """
""" 
x = 1   # int
y = 2.8 # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))
 """

# Int
# Integer is a whole number, positive or negative without decimal, of unlimited length
""" 
x = 1
y = 9719123129812398213
z = -38273

print(type(x))
print(type(y))
print(type(z))
 """

# Float
# "Floating point number" is a number, positive or negative, containing one or more decimals.
""" 
x = 1.0
y = 1.133
z = -33.83

print(type(x))
print(type(y))
print(type(z))
 """

# Complex 
# Complex numbers are written with "j" as the imaginary part
""" 
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
 """

# ? Type Conversion
# Can convert numbers from one type to another by using int(), float() or complex() methods
""" 
x = 1     #int
y = 2.5   #float
z = 1j    #complex

# Convert Int to Float
a = float(x)

# Convert float to Int
b = int(y)

# Convert Int to Complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
 """

# ? Random Numbers
# use the random() module to generate random numbers
import random

print(random.randrange(1, 10))