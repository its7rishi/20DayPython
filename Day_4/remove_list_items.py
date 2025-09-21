# * REMOVE LIST ITEMS


# remove()
# to remove a specific item from the list
# if there are more than one occurrence of the item,
# The first occurrence is removed.
""" 
myList = ['apple', 'banana', 'cherry']
myCars = ['ford', 'toyota', 'suzuki', 'toyota']
myList.remove('banana')
myCars.remove('toyota')
print(myList)
print(myCars)
 """

# pop()
# remove specified index
""" 
myList = ['apple', 'banana', 'cherry']
myList.pop(1)
print(myList)
 """

# if index is not specified pop() will remove the last item from the list
""" 
myList = ['apple', 'banana', 'cherry']
myList.pop()
print(myList)
 """

# * DEL keyword
# the del keyword removes an item from the specified index

myList = ['First', 'Second', 'Third']
""" 
del myList[1]
print(myList)
 """

# The del keyword can also delete the list completely
""" 
del myList
print(myList) # NameError: name 'myList' is not defined
 """

# * CLEAR THE LIST
# clear() method

myList = ['India', 'Bangladesh', 'Nepal']
myList.clear()
print(myList) # []