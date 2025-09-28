""" DOCSTRINGS """

def add_numbers(a,b):
  """ 
   Adds two number and returns their sum.

   Parameters
   __________

   a: int or float
      The first number to be added

  b:  int or float
      The second number to be added

  Returns 
  ________

  int or float
      The sum of 'a' and 'b'
     """
  return a + b

print(add_numbers(2,3))
print(add_numbers.__name__)
print(add_numbers.__doc__)