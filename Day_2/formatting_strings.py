# F-Strings

# To specify a string as an f string
# add an f in front of the string
# and a placeholder in for variables in curly brackets
""" 
price = 55
txt = f"The price is {price} dollars"
print(txt)  # The price is 55 dollars
 """

# Placeholders & Modifiers
# Placeholders can contain variables, operations, functions and modifiers
""" 
price = 99
txt = f"The price is {price:.2f} dollars."
print(txt)  # The price is 99.00 dollars
 """

# Placeholders can contain Python code
""" 
txt = f"The price is {20 * 50} dollars"
print(txt)  # The price is 1000 dollars

 """

# ? Escape Characters

""" 
Below text will give an error as you cannot
enter double quotes inside double quotes

txt = "We are the "Vikings" from the North."
 """

# To fix above issue, use an escape character '\' 

txt = "We are the \"Vikings\" from the North."
print(txt)  # "We are the "Vikings" from the North."

""" 
List of Escape Characters:

\'    - Single Quote
\\    - Backslash
\n    - New Line
\r    - Carriage Return
\t    - Tab
\b    - Backspace
\f    - Form Feed
\ooo  - Octal Value
\xhh  - Hex Value 
 """