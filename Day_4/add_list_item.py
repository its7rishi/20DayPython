# Add List Item

# append() = To append and item at the end of the list
myList = ['apple', 'banana', 'cherry']
""" 
myList.append('kiwi')
print(myList)
 """

# insert() - to insert an item at a specified index
""" 
myList.insert(1, 'mango')
print(myList)
 """

# * EXTEND LIST
# ? To append elements from another list to the current list
""" 
berries = ['strawberry', 'raspberry', 'blueberry']
myList.extend(berries)
print(myList)
 """
# * Add Any Iterable
# ? The extend command allows you to add any iterable object (tubples, sets, dictionaries)
""" 
myTuple = ('pineapple', 'papaya', 'melon')
myList.extend(myTuple)
print(myList)
 """
