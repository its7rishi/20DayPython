def calculate():
  x = int(input("Enter first number: "))
  y = int(input("Enter second number: "))
  choice = int(input("Choose 1 to Add \n Choose 2 to Subtract \n Choose 3 to Multiply \n Choose 4 to Divide \n Choose 0 to exit \n"))
  if choice == 1:
    print(f"The sum is: {x + y}")
  elif choice == 2:
    print(f"The difference is: {x - y}")
  elif choice == 3:
    print(f"The product is: {x * y}")
  elif choice == 4:
    print(f"The result of division is: {x / y}") 
  elif choice == 0:
    print(f"Bye Bye, See you again soon")
  else:
    print("Please make a valid choice")
    return
calculate()