# Values created outside a function are global variables
# Can be used both inside and outside a function
""" 
x = "awesome"

def myFunc():
  print("Python is " + x)

myFunc()
 """

# ? Variable with same name inside a function is treated as local and will be used only inside the function
""" 
x = 'awesome'

def myFunc():
  x = 'great'
  print("Python is " + x)

myFunc()

print("Python is " + x)
 """

# global keyword -> To create a global variable inside a function, use the global keyword

def myFunc():
  global x
  x = 'apple'

myFunc()

print("My favorite fruit: " + x)