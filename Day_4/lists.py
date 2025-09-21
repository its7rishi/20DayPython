# Python Lists
""" 
myList = ['apple', 'banana', 'cherry']
myNums = [1,2,3,4,5]
 """

# Length
# ? len() function
""" 
fruits = ["apple", "banana", "cherry", "dragon fruit"]
print(len(fruits))
 """

# list datatype
# lists are defined as objects with class 'list'
# use the 'type()' function to get the type
""" 
myList = [1,3,4,3,2]
print(type(myList))
 """

# The List Constructor
# You can create a list using the 'list()' constructor
""" 
myList = list(('apple', 'banana', 'cherry'))
print(myList)
 """

# * COLLECTION DATA TYPES
#   ? There are 4 Collection Data Types in Python
# 1. List - a collection which is ordered and changeable. Allows duplicate items
# 2. Tuple  - a collection which is ordered and unchangeable. Allows duplicate items
# 3. Set    - a collection which is unordered, unchangeable and un-indexed. No duplicate items are allowed. 
# 4. Dictionary - a collection which is ordered and changeable, No duplicate members
# 3. 
# ! Set items are unchangeable but you can add / remove items in a Set


# Access List Item
""" 
names = ['Alex', 'Barry', 'Celina', 'Dino', 'Elijah', 'Frank', 'George', 'Henry']

# By Index No.
print(names[2]) # Celina

# Negative Indexing
print(names[-2])  # George

# Range of indexes
print(names[2:5]) # ['Celina', 'Dino', 'Elijah']
print(names[3:])  # ['Dino', 'Elijah', 'Frank', 'George', 'Henry']
print(names[:6])  # ['Alex', 'Barry', 'Celina', 'Dino', 'Elijah', 'Frank']

# Range of Negative Indexes
print(names[-4: -1])  # ['Elijah', 'Frank', 'George']

# Check if item exists in the list
if 'Henry' in names:
  print('Yes, Henry is present')
 """

# changing List item

cars = ['Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Toyota']

# By index number
cars[2] = 'Porsche'
print(cars)

# Change range of values
cars[1:3] =   ['Bugatti', 'Volvo']
print(cars)

# ? If more items are inserted than you replace,
# ? The new items will be inserted where you specified
""" 
shoes = ['adidas', 'nike', 'reebok']
# if you add more items than you replace, the extra items will be inserted. The remaining items will move accordingly
shoes[1:3] = ['hush puppies', 'skechers', 'bata', 'crocs']
# if you add lesser items than you want to replace, the new item will ben inserted and the remaingin itemsw will move accordingly
shoes[1:3] = ['woodland']
print(shoes)
 """

# Insert Item
# to insert an item into the list without replacing any item.
""" 
myList = ['A', 'B', 'C', 'D', 'E', 'F']
myList.insert(2, 'Z')
print(myList)
 """