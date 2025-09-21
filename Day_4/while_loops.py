# While Loops
""" 
i = 1
while i < 6:
  print(i)
  i += 1
   """

# Break Statement
# Used to stop the loop
""" 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
   """

# Continue 
# continue statement breaks the current iteration of the loop
# and continues with the next iteration
""" 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
   """

# Else 
# else statement runs a block of code once the while condition is no longer true

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")