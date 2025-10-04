""" PYTHON TRY EXCEPT """

# ? try - try block lets us tet a block of code for errors
# ? except = except block lets you handle the error
# ? else = else block lets you execute code when there is no error
# ? finally - finally block lets you execute code regardless of the try and except blocks

# * EXCEPTION HANDLING
# When and error / exception occurs, Python will stop and generate an error message
# These exceptions are handled using try statement

# Example: 
""" 
try:
  print(x)
except:
  print('An error has occurred')
 """

# * Many Exceptions
# ? We can define multiple exceptions
""" 
try:
  print(x)
except NameError:
  print("variable x is not defined")
except:
  print("Something else went wrong")
   """

# * Else
# ? we can use else to define a block of code ir there are no errors

# Example:
""" 
try:
  print("hello")
except:
  print('Something went wrong')
else:
  print("nothing went wrong")
   """

# * Finally
# ? Finally block, if specified will be executed regardless if the try block raises an error or not
""" 
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("Try and except finished")

 """  

# ? This can be useful to close objects and clear up resources
""" 
try:
  f = open("demo.txt")
  try:
    f.write("Lorem Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print('Something went wrong when opening the file')
   """

# * Raise exception

# ? We can also throw / raise and exception in Python
# ? To throw or raise an exceptions use the ' raise ' keyword

# Example:
""" 
x = -1

if x < 0:
  raise Exception('Sorry! No number allowed below 0')
 """

# ? we can also choose the type of error to be raised

# Example:

x = 'Hello'

if not type(x) is int:
  raise TypeError("Only Integers are allowed")