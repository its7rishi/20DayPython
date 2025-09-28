""" LAMBDA FUNCTIONS """

# * Lambda Functions
# ? A lambda function is a small anonymous function
# ? It can take any number of arguments bur can have only one expression

# ? Syntax: lambda arguments : expression
""" 
x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(3,4))

z = lambda a, b, c : a + b + c
print(z(5, 6, 7))
 """

# Using lambda inside a function
""" 
def myFunc(n):
  return lambda a : a * n

myMultiplier = myFunc(5) # Sets the value of n in myFunc

print(myMultiplier(3)) # Output: 15

def newFunc(n):
  return lambda a : a ** n

myExpo = newFunc(3)

print(myExpo(5))

 """

# Use same function definition to make both functions, in the same program

def myFunc(n):
  return lambda a : a * n

myDoubler = myFunc(2) # Sets the value of n in myFunc as 2
myTripler = myFunc(3) # Sets the value of n in myFunc as 3

print(myDoubler(5)) # Output: 10
print(myTripler(6)) # Output: 18