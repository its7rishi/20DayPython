# Boolean Values
""" 
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
 """

""" 
a = 200
b = 15

if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")
   """

# Evaluate values
""" 
print(bool("hello")) # True
print(bool(14)) # True
 """

# Most Values are true
# Any String is True except empty strings
# Any Number is true except 0
# Any list, tuple, dictionary are True, except empty ones
""" 
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(False))  # False
print(bool(None))  # False
print(bool(()))  # False
print(bool({}))  # False
 """

# Object made from a class with __len__ function returns 0 or False
""" 
class myClass():
  def __len__(self):
    return 0
  
myObj = myClass()
print(bool(myObj))  # False
 """

# ? Functions can return Boolean
""" 
def myFunction():
  return True

print(myFunction())
 """

# ? Many built-in functions like the 'instance()' function can also return Boolean.

x = 200
print(isinstance(x, int)) # True