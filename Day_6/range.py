""" RANGE """

# * range() function
# ? The built-in range() function generates an immutable sequence of numbers
# ? Commonly used for looping a specific number of times

# Creating ranges

# The range() can be called wih 1, 2 or 3 arguments

""" 
Syntax:
range(arg1, arg2, arg3)

arg1 -  starting number
arg2 -  number upto which the sequence should be (not including)
arg3 = step value i.e., the difference between each number. If not provided, the default value is 1

? range(3,10, 2) = returns a range from 3 to 9 with a step of 2
 """
""" 
# range with 1 argument

x = range(10)

# display x
print(x)

# convert to list to display content of x
print(list(x))

# * Call range with 2 arguments

y = range(3,10)

print(y)

print(list(y))


# * Call range with 3 arguments

z = range(3, 10, 2)

print(z)
print(list(z)) 
"""

# * Using ranges
for i in range(10):
  print(i)

# * Using list to display ranges
""" 
print(list(range(5)))
print(list(range(1,6)))
print(list(range(5, 20, 3)))
 """

# * Slicing ranges
""" 
r = range(10)
print(r[2])
print(r[:3])
print(r[1:])
 """
# Membership Testing

r = range(0, 10, 2)

print(6 in r)
print(7 in r)

#Length
print(len(r))