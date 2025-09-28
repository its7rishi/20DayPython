""" A Project to check Prime Number
    _______________________________

    1. Takes an int as an input.
    2. Checks whether it is a prime number
    3. Returns " Yes, it is a prime number" if true
    4. Returns "No, it is not a prime number" if false
 """

def is_prime():
  print('Welcome to Prime Number Checker')
  user_input = int(input("Enter a number to check if it is a prime number: "))
  # user_input = 36 # for testing
  

  if user_input <= 1:
    return f"No, {user_input} is not a prime number"
  
  if user_input == 2:
    return f"Yes, {user_input} is a prime number"
  
  i = 2

  while i * i <= user_input:
    if user_input % i == 0:
      return f"No, {user_input} is not a prime number"
    i += 1
  
  return f"Yes, {user_input} is a prime number"

  

print(is_prime())