""" USER INPUT """

# ? Helps to ask the user for an input

""" 
  * Python stops executing when it comes to the input() function and continues after the user has provided an input
 """

# Example:
""" 
print("Enter your name: ")
name = input()
print(f"Hello {name}")
 """

# ? Python input() has a prompt parameter, which acts as a message we can put in front of the user input on the same line.
""" 
name = input("What is your name?: ")
print(f"Hello {name}")
 """

# ? Multiple inputs can be added

# Example:
""" 
name = input("Enter your name: ")
print(f"Hello {name}")
fav1 = input("What is your favourite animal: ")
fav2 = input("What is your favourite colour: ")
fav3 = input("What is your favourite number: ")
print(f"Fo you want a {fav2} {fav1} with {fav3} legs?")
 """

# * Input Number
# ? input from user is treated as a string
# ? You can convert the input into a number using the float() function

# Example
""" 
import math
x = input("Enter a number: ")

# Find square root of the number
y = math.sqrt(float(x))

print(f"The square root of {x} is : {y}")
 """

# * Validate a number
# ? It is a good practice to validate user input.
# ? to avoid getting error, we can test the user input
# ? we can ask a user to retry with a message

y = True
while y == True:
  x = input("Enter a number: ")
  try:
    x = float(x)
    y = False
  except:
    print('Wrong input, please try again')

print("Thank you!")