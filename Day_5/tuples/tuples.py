""" TUPLES """
# ? Collection data type in python
# ? ordered and unchangeable
# ? written with round brackets
""" 
myTuple = ('apple', 'banana', 'cherry')
print(myTuple)

# * Tuple Items
# ? Tuple items are ordered, unchangeable and allow duplicates

fruitTuple = ("apple", "banana", "cherry", "banana", "cherry")

# * Tuple with single item
# A tuple with single item can be created
# A comma is needed at the end
singleTuple = ('pineapple',)
print(type(singleTuple))

# * TUPLE CONSTRUCTOR
# use the tuple() constructor

car_tuple = tuple(("BMW", "Ferrari", "Audi"))
print(type(car_tuple))
 """

# * ACCESS TUPLES

""" 
fruits = ("apple", "banana","cherry", "mango","kiwi", "peach")
print(fruits[1])
print(fruits[-2])
print(fruits[2: 5])
print(fruits[:4])
print(fruits[2:])
print(fruits[-3: -1])
 """

# * Check if item exists in tuple
""" 
if 'cherry' in fruits:
  print('cherry is present in fruits')
 """

# * UPDATE TUPLES
# Once created, the tuple values cannot be changed
# Tuples are unchangeable or immutable
# ? WORKAROUND = convert tuple to a list, make changes and change it back to tuple
""" 
myTuple = ('Delhi', 'Kolkata', 'Mumbai', 'Pune')
mylist = list(myTuple)
mylist[1] = "Gwalior"
myTuple = tuple(mylist)
print(myTuple)

# Add Items
# Method 1: Convert to list
mylist2 = list(myTuple)
mylist2.append('Chennai')
myTuple = tuple(mylist2)
print(myTuple)

# Method 2: Add tuple to tuple
my_newTuple =('Lucknow',)
myTuple += my_newTuple

print(myTuple)
 """

# * Remove Items 
# Tuples are immutable, hence we cannot remove items
# ? WORKAROUND: Change to a list
""" 
names = ('John', 'Eric', 'Ben')

y = list(names)
y.remove('Eric')
names = tuple(y)
print(names)
 """

# * DELETE TUPLE
""" 
myTuple = ("a", "b", "c")
del myTuple
print(myTuple)  # We get an error as the tuple has been deleted
 """
# * UNPACK TUPLES

# When you create a tuple, it is called packing a tuple

fruits = ('apple', 'banana', 'cherry') # packing

# (green, yellow, red) = fruits # unpacking tuple

# number of variables should match the number of values in tuple

# print(green)
# print(yellow)
# print(red)

# * USING ASTERISK(*)
# if number of variables is less than number of values
# we can add an '*' to the variable name
# the values will be assigned to the variable as a list
""" 
fruits = ('apple', 'banana', 'cherry', 'mango', 'strawberry', 'pineapple')

(green, yellow, *red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'mango', 'strawberry', 'pineapple']

# if the asterisk is added to another variable other than the last
# Python will assign values to the variable until the number of
# values left matches the number of variables left

(one, *two, three) = fruits
print(one) # apple
print(two) # ['banana', 'cherry', 'mango', 'strawberry']
print(three) # pineapple
 """

 # * Loop Through Tuples

 # for loop

movies = ("Spiderman", "Batman", "Superman ")
""" 
for x in movies:
 print(x)
 """
 # Loop through Index Numbers
 # using range() and len()
""" 
for x in range(len(movies)):
  print(movies[x])
 """

# Using While Loops
""" 
i = 0
while i < len(movies):
  print(movies[i])
  i += 1
 """

# * JOIN TUPLES
""" 
# USING '+'
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
 """

# * MULTIPLY TUPLES
""" 
fruits = ('Apple', 'Banana', 'Cherry')
nums = (1, 2, 3)
my_tuple = fruits * 2
num_tuple = nums * 3
print(my_tuple)
print(num_tuple)
 """

# * TUPLE METHODS

# Count - count()
# Returns number of times a specified value occurs in the tuple.

fruits = ("apple", "banana", "cherry")
num = fruits.count("banana")
print(num)

# index()
# returns the position of the specified variable in the tuple

pos = fruits.index("cherry")
print(f"cherry is at index number {pos} position in the tuple")