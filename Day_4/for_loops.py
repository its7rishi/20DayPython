# For Loops
# used to iterate over 
# lists, tuple, dictionary, set or string
""" 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
   """

# Looping through a string
""" 
for x in "banana":
  print(x)
   """

# Break statement
""" 
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  print(x)
  if x == 'banana':
    break
   """

# Continue Statement
""" 
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  if x == 'banana':
    continue
  print(x)
   """

# Range function
# used to loop through a set of code specified number of times
# it starts from 0 upto 1 less than the number specified
# Example: range(6) = 0, 1, 2, 3, 4, 5
""" 
for x in range(6):
  print(x)
 """

# Change Starting value
# range(1, 6) = from 1 upto 6, but not including 6
""" 
for x in range(2, 6):
  print(x)
   """

# Skip the increment
# The 3rd parameter in range function is used to specify the skip value
# Example: range(1, 30, 3) => 1, 4, 7,....,
""" 
for x in range(2, 30, 3):
  print(x)
   """

# Else in For Loop
# used to execute a code after the for loop has ended
""" 
for x in range(6):
  print(x)
else:
  print('Finally finished!')
 """  

# break
# ! Else will not execute if there is a break statement in the for loop
""" 
for x in range(6):
  if x == 3: break
  print(x)
else:
  print('Done!')
 """  

# Nested Loops
""" 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x,y)
     """

# Pass statement
# If for loop has no content
# use pass statement to avoid getting errors

for x in range(6):
  pass