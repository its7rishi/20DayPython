""" DECORATORS """

# Decorators are functions that take another function as an input
# and return a new function

# ? define decorator with ' @decorator_name ' above the function

# * Decorators can be called multiple times

# def change_case(func):
#   def myWinner():
#     return func().upper()
#   return myWinner

# @change_case
# def myFunction():
#   return 'Hello Sally'

# print(myFunction())

""" 
By placing @change_case above myFunction, myFunction is being decorated with the change_case function

*The function 'change_case' is the decorator
 """


""" 
def change_case(func):
  def myWinner():
    return func().upper()
  return myWinner

@change_case
def otherFunction():
  return "I am speed"

@change_case
def anotherFunction():
  return "There is no price for awesomeness, or attractiveness"

@change_case
def eiSaala():
  return "Ei Sala Cup Namde!"

print(otherFunction())
print(anotherFunction())
print(eiSaala())
 """

# * Arguments in Decorated Functions

# ? Functions requiring arguments can also be decorated

""" 
def changeCase(func):
  def myWinner(x):
    return func(x).upper()
  return myWinner

@changeCase
def someText(name):
  return "Hello " + name


print(someText('david'))
 """


# ? *ars and 8kwargs
# Sometimes decorator functions have no control over the arguments passed from decorated functions.
# To solve this problem, add (*args, **kwargs) to the wrapper function.
# The wrapper function can now accept any number and any type of argument and pass them to decorated functions
""" 
def changeCase(func):
  def myWinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myWinner


@changeCase
def myFunction(name):
  return "Hello " + name

@changeCase
def fullName(fname, lname):
  return f"Hello {fname} {lname}"

print(myFunction(name = 'Prachi'))
print(fullName(fname='Sunil', lname='Gavaskar'))
 """

# * DECORATOR WITH ARGUMENTS

# ? Decorators can accept their own arguments by adding another wrapper level
""" 
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

@changecase(2)
def myNewFunction():
  return "Hello Grandpa"

print(myfunction())
print(myNewFunction())
 """

# * MULTIPLE DECORATORS

# ? You can have multiple decorators on one function
# ? This is done by placing the decorators on top of each other
# ? The decorators are called in the order they are specified.
""" 
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
 """

# * PRESERVING FUNCTION METADATA

# ? Function metadata can be accessed through the __name__ and __doc__ attributes
""" 
def myFunction():
  return "Have a great day"

print(myFunction.__name__)
 """
# ? When a function is decorated the metadata of the original function is lost

""" 
def changecase(func):
  def myWinner():
    return func().upper()
  return myWinner

@changecase
def myFunction():
  return "Have a great day!"

print(myFunction.__name__) # myWinner => from the decorator functions
 """

# ? Python built-in function called ' functools.wraps ' can be used to preserver the original function's name and docstring

# ? Import functools.wraps to preserve the original function name and docstring
""" 
import functools

def changecase(func):
  @functools.wraps(func)
  def myWinner():
    return func().upper()
  return myWinner


@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

 """

def changecase(func):
  def wrapper():
    return func().upper()
  return wrapper

def exclaim(func):
  def wrapper():
    return func() + "!"
  return wrapper

@changecase
@exclaim
def myFunc():
  return "Hello"

print(myFunc())