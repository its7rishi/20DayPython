""" 
FACTORIAL CALCULATOR
____________________

A program to calculate the factorial of a given number

1. Takes an int as an input
2. Calculates the factorial
3. Returns the factorial value
 """

# Function to calulate factorial
def factorial(num):

  i = num
  result = 0

  if num == 0 or num == 1:
    return 1
  
  while i > 1:
    return i * factorial(i -1)
  
  i -= 1

# function to get user input and check if the input is positive integer
def getInput():
  print("\n WELCOME TO THE FACTORIAL CALCULATOR\n____________________________________\n\n")

  user_input = int(input("Enter a number to calculate it's factorial: "))

  if user_input < 0:
    print("Enter positive integers only")
    return

  print(f"The factorial of {user_input} = {factorial(user_input)}")

getInput()