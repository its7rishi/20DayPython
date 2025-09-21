# * LIST COMPREHENSION

# used to create an new list based on existing list

# ? Without List comprehension, using a for loop

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newList = []

for x in fruits:
  if "a" in x:
    newList.append(x)

print(newList)  # ['apple', 'banana', 'mango']

# * shorter syntax with list comprehension - 1 line
compList = [x for x in fruits if 'a' in x]
print(compList) # ['apple', 'banana', 'mango']

withoutA = [x for x in fruits if 'a' not in x]
print(withoutA) # ['cherry', 'kiwi']

# * without if condition
# if condition is optional

noIf = [x for x in fruits]
print(noIf)

# * ITERABLE
# The iterable can be any iterable object like a list, tuple, set, etc.

numList = [x for x in range(10)]
print(numList)

lessThan5 = [x for x in range(10) if x < 5]
print(lessThan5)

upper_Case = [x.upper() for x in fruits]
print(upper_Case)

orangy = [x if x != 'banana' else 'orange' for x in fruits]
print(orangy) # ['apple', 'orange', 'cherry', 'kiwi', 'mango']