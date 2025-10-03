""" STRING FORMATTING """

# * F-STRINGS (Python 3.6+)
# Before Python 3.6, we used the format() method to format strings.
# ? F-String allow you to format selected parts of a string
# ? To specify a string as an f-string, simply put an ' f ' before th string.

# Example 1
""" 
txt = f"The price is 49 dollars"
print(txt)
 """
# * Placeholders & Modifiers
# ? To format values in a string, use a placeholder { } in the string.
# ? Placeholders can contain variables, functions, operations and modifiers to format the value.
""" 
price = 59
txt = f"The price is {price} dollars"
print(txt)
 """

# ? The placeholder can also contain a modifier to format the value.
# ? The modifier is added after a colon : inside the placeholder.


# # Example 2
# price = 49

# txt = f"The price is {price:.2f} dollars"

# print(txt)  # The price is 49.00 dollars

# # ? You can format a string directly without keeping a variable

# print(f"The temperature is {34:.2f} degrees celsius")  # The temperature is 34.00 degrees celsius

# * Operations in F-Strings
# ? You can also perform operations inside the placeholder { }.
""" 
price = 59
tax = 0.25

txt = f"The price is {price * (1 + tax):.2f} dollars"

print(txt)  # The price is 73.75 dollars

 """

# ? You can perform if...else statements inside the placeholder { }.
# ? The if...else statement must be in one line.
# ? The if...else statement must be after the value to be evaluated.
# ? The if...else statement must be separated by a colon :.
# ? The if...else statement must be inside the placeholder { }.
# ? The if...else statement must be inside the f-string.
""" 
price = 54
txt = f"The price is very {"Expensive" if price > 50 else "Cheap"}"

print(txt)  # The price is very Cheap
 """

# * Execute functions in F-Strings
""" 
fruits = "pineapples"

txt = f"I love {fruits.upper()}"

print(txt)  # I love PINEAPPLES
 """
""" 
def my_converter(x):
  return x * 0.3048

txt = f"The plane is flying at a height of {my_converter(30000)} meters altitude"

print(txt)  # The plane is flying at a height of 9144.0 meters altitude
 """

# * More Modifiers

# Use comma as a thousand separator
""" 
price = 59000
txt= f"The price is {price:,} dollars"
txt2 = f"The price is {price:_} dollars"  # Using underscore as a thousand separator (Python 3.6+)
txt3 = f"The price is {price:n} dollars"  # Using locale-aware separator (Python 3.6+)
print(txt)
print(txt2)
print(txt3)
 """

# * String format()
""" 
price = 40
txt = "The price is {} dollars"
deci = "The price is {:.2f} dollars"
print(txt.format(price))  # The price is 40 dollars
print(deci.format(price))  # The price is 40.00 dollars
 """

# * Multiple Values
price = 49
itemno = 467
quantity = 3
myOrder = "I want {} pieces of item number {} for a price of {} dollars."
print(myOrder.format(quantity, itemno, price))  # I want 3 pieces of

# * Index Numbers
# ? You can use index numbers {0}, {1}, {2} to be sure the values are placed in the correct placeholders.
# ? The index numbers refer to the position of the values in the format() method.
# ? The index numbers start at 0.
""" 
myNew_Order = "I want {0} pieces of item number {1} for a price of {2:.2f} dollars."
print(format(myNew_Order.format(quantity, itemno, price)))  # I want 3 pieces of item number467 for a price of 49.00 dollars.
 """
""" 
age = 39
name = "Brian"
txt =  "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
 """

# * Named Indexes
# ? You can also use named indexes {carname}, {model} in the placeholders.
# ? The named indexes must be the same as the names of the parameters in the format() method.
# ? The order of the parameters does not matter.

myCar = "I have a {carname}, it is a {model}."
print(myCar.format(carname = "Ford", model = "Mustang"))  # I have a Fort, it is a Mustang.