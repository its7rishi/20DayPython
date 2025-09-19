# Strings

# String are surrounded by single (') or double("") quotes.
""" 
print("Hello")
print('Hello')
 """

# ? Quotes Inside Quotes
# Can use quotes inside other quotes as long as they don't match
""" 
print("It's all right.")
print("Mickey says 'Hi!'.")
 """

# ? Multiline String
# Can assign multiline texts using 3 quotes (single/ double)

# a = """this is the first line,
#   This is the second line,
#   This is the third line
#   """

# print(a)

# # or 3 single quotes

# b = '''This is the first line,
# This is the second line,
# This is the third line.'''

# print(b)

# String are Arrays
""" 
a = "Hello World"
print(a[2]) # output: l
 """

# ? Looping through strings
""" 
fruit = "banana"
for x in fruit:
  print(x) # prints out each letter of the variable fruit
   """

# ? String Length
# To get the length of a string, use the len() function
a = "Hello, Coders!"
print(len(a))   # prints 14

# ? Check String
# To check if a certain character or word is present in the string, use the 'in' keyword
""" 
text = "A hot cup of coffee can fix all problems."
print("hot" in text)  # returns True
print("zebra" in text)  # returns False
 """

# ? Check If Not
# To check if a certain phrase or character is not present in the string, use 'not in' keyword
""" 
text = "A hot cup of coffee can fix all problems."
print("apple" not in text)  # returns True
print("coffee" not in text) # returns False
 """

# ? Slicing Strings
# A string can be sliced to return a string of characters

# b = "Hello, World!"
# print(b[2:5])   # Prints from position 2 to 5 (not including 5)
# print(b[:5])  # prints from the start to position 5 (not including 5)
# print(b[2:])  # prints from position 2 to the end of string.

# ? Negative Indexing
# Use negative indexing to start the slice from the end of the string

# txt = "Hello, World"
# print(txt[-5 : -2]) # slices the string from position -5 to position -2

# ? Modify String
""" 
txt = "Hello, World!"
text2 = "   Hello, World!    "
print(txt.upper())  # prints the string in uppercase
print(txt.lower())  # prints the string in lowercase
print(text2)
print(text2.strip()) # removes whitespace from the beginning or the end of string
 """

# ? Replace String

# Replace a string with another string using 'replace()' method
""" 
txt = "Hello, World!"
print(txt.replace("H", "J"))  # Prints 'Jello World!'
 """

# ? Split String
# 'split()' method splits a string using using a separator and returns a list (if the separator is found)
""" 
text = "Hello, World!"
print(text.split(","))  # returns ['Hello', 'World!']
 """