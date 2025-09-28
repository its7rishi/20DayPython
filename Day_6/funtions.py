""" FUNCTIONS """

def myFunction():
  print("Hello, World!")

# myFunction()

# function with arguments
""" 
def names(fname):
  print(fname + ' Bose')

names('Jack')
names('Dennis')
names('Julie')
 """

# if you call a function with extra arguments, you will get an error

def sum(x, y):
  result = x + y
  print(result)

# sum(3, 4, 7) # ! Gives an error due to extra argument

# * Arbitrary Arguments, *args
# ? If number of arguments are unknown, add a ' * ' before the parameter name in function definition
# ? The function will receive a tuple of orguments and can access them accordingly
""" 
def kiddos(*kids):
    print(kids)
    for x in kids:
      print(x)

kiddos('Jake', 'Paul', 'Nyla')
 """

# * KEYWORD ARGUMENTS

# ? You can send arguments with key = value syntax
# ? This way, the order of the arguments will not matter
""" 
def hello(name1, name2, name3):
  print(f"Hello {name2}")


hello(name1= 'Adam', name3= 'Thomas', name2= 'Celina')
 """

# * ARBITRARY KEY WORD ARGUMENTS

# ? If you are unsure how many keyword arguments would be passed,
# ? add ' ** ' before the parameter in function definition
# ? The function will receive a dictionary of arguments and can access them accordingly.
""" 
def name_print(**kwargs):
  print(f"His first name is {kwargs["fname"]} and his last name is {kwargs["lname"]}")

name_print(fname="Clark", lname = "Kent")
 """

# * DEFAULT PARAMETER VALUE
# ? If we call the function without arguments, it uses the default value
""" 
def myFunc(country = 'Belarus'):
  print(f" {country} is beautiful")

myFunc('India') # with argument
myFunc() # without argument
 """

# * PASS A LIST OF OF ARGUMENTS
""" 
def myFood(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

myFood(fruits)
 """

# * RETURN VALUES
# ? for the function to return a value, use the ' return ' statement
""" 
def sum(a, b):
  return a + b

print(sum(5, 3))
 """

# * PASS STATEMENT
# ? Function statements cannot be empty.
# ? If it is empty, use a ' pass' statement to avoid errors
""" 
def myTest():
  pass

myTest() # No errors
 """

# * POSITIONAL-ONLY ARGUMENTS
# ? You cna specify that a function can have ONLY positional arguments or ONLY keyword arguments
""" 
def my_function(x, /):
  print(x)

my_function(3) # positional argument is accepted
#my_function(x = 3) # ! keyword keyword fives an error

# ? without ' ,/ ' you can pass keywor arguments without error

def someFunc(a):
  print(a)

someFunc(a = 'Peacock')
 """

# * KEYWORD ONLY ARGUMENTS
# ? To specify that a function can have only keyword arguments
# ? user ' *, ' before the arguments
""" 
def keywordFunc(*, x):
  print(x)

keywordFunc(x = 'apple') # with keyword argument 
# keywordFunc('apple') # ! Error without keyword argument

# ? Without ' *, ', you can pass keyword arguments 

def noKey(x):
  print(x)

noKey(x = 'banana')
 """

# * COMBINE Positional-Only and Keyword-Only
# ? Both the arguments can be defined in the same function
#? Any arguments before ' /, ' will be positional arguments
# ? Any arguments after ' *, ' will be keyword arguments
""" 
def function(a, b, /, *, c, d):
  # a & b are positional arguments
  # c & d are keyword arguments
  print(a + b + c + d)

function(2, 3, c = 5, d = 8)
 """

# * RECURSION
# ? Recursion means that a function can call itself

# ! EXIT CLAUSE: Remember to always provide an exit clause to a recursive function, else it will keep running endlessly

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  
  return result

print(tri_recursion(6))

""" 
Recursion Order: 
f(6) = 6 + f(5) 6 + 15 = 21
f(5) = 5 + f(4)  5 + 10 = 15
f(4) = 4 + f(3) = 4 + 6 = 10
f(3) = 3 + f(2) = 3 + 3 = 6
f(2) = 2 + f(1) = 2 + 1 = 3
f(1) = 1 + f(0)  = 1 + 0 = 1

Result Order:
1
3
6
10
15
21
21
 """