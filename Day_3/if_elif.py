# IF ELSE
""" 
a = 200
b = 300

# if statement
if a > b:
  print('A')

# elif statement
if a > b:
  print('A')
elif b > a:
  print('B')

 # else statement
if a > b:
  print('A')
elif b > a:
  print('B')
else:
  print('A = B')

# Ternary Operator

# Short Hand if
if(a < b): print('A is smaller')

# Short had if else
print('A') if a > b else print('B')

# if else statement with 3 conditions
print('A') if a > b else print('=') if a == b else print('B')
 """
""" 
# AND
a = 200
b = 33
c = 500

if a > b and c > a:
  print('Both the conditions are true')

# OR

if a > b or a > c:
  print("At least one of the conditions is true")

  # NOT
if not a > c:
  print("A is NOT greater than C")

 """
""" 
# NESTED IF
x = 14

if x > 10:
  print("Above 10")
  if x > 20:
    print("and also above 20")
  else:
    print("but not above 20")
     """

# Pass
# If statements cannot be empty 
# But if for some reason if has no content
# use 'pass' statement to avoid getting an error
a = 33
b = 200

if b > a:
  pass