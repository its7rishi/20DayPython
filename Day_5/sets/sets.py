""" SETS """

# ? A collection data type in Python
# ? There are Unordered, Un-indexed and Unchangeable
# ? Do not allow duplicate
# ! SET items are unchangeable but can be removed and new items can be added

# my_set = {'apple', 'banana', 'cherry', 'apple'}
# print(my_set) # Duplicate value gets removed ['apple', 'banana', 'cherry']

# True and 1 are considered the same value
""" 
randomSet = {'apple', 'banana', 'cherry', True, 1, 2}
print(randomSet) # 1 is removed as True and 1 are considered same

# False and 0 are considered same
thisset = {True, False, 2, 0, 9}
print(thisset) # 0 is removed as False and 0 are considered same
 """

# * Length of set
# use len() method
""" 
candies = {'snickers', 'mars', 'skittles'}
print(len(candies))
 """

# * SET CONSTRUCTOR
# use set()
""" 
fruits = set(('apple', 'banana', 'cherry', 'mango'))
print(fruits)
 """

# * ACCESS SET ITEMS

# ? We cannot access set items using index or key
""" 
myset = {"China", "India", "Russia"}

for x in myset:
  print(x) # prints all the items in the set

print("banana" in myset) # prints True if "banana" is present else False

print("banana" not in myset) # prints True if "banana" is not present else False

# * Change Set Items
# ? Set Items cannot be changed once it has been created

mylist = list(myset)
print(mylist)
mylist[0] = 'Nepal'
myset = set(mylist)
print(myset)
 """

# * ADD SET ITEMS
# Any iterable can be added to the set
# use update() command
""" 
thiset = {"apple", "banana", "cherry"}
thiset.add("apricot")
print(thiset)
 """
# * ADD SETS
# ? you can add any iterable
""" 
set1 = {"A", "B", "C"}
set2 = {"D", "E", "F"}
list1 = [2, 3, 4]

# set1.update(set2)
set1.update(list1)
print(set1)

 """

# * REMOVE SET ITEMS
# remove() method
# ! If the item to remove does not exist, it will throw error
""" 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# thisset.remove("peach") # KeyError: 'peach'
print(thisset)
 """

# discard() method
# ? If the item to remove is not present, no error will be thrown
""" 
thisset = {"Ford", "Ferrari", "Mercedes"}
thisset.discard("Ford")
thisset.discard("Audi")
print(thisset)
 """

# pop() method
# does not take any argument
# ? It randomly removes an item
# ? Sets are unordered, while using pop(), you do not know which item will be removed from the set.
""" 
thisset = {"Whiskey", "Martini", "Wine"}
thisset.pop()
print(thisset)
 """

# * EMPTY THE SET

# clear() - method
""" 
thisset = {"Oxygen", "Hydrogen", "Nitrogen"}
thisset.clear()
print(thisset)
 """

# * DELETE THE SET

# del keyword
""" 
thisset = {"Gold", "Silver", "Titanium"}
del thisset
print(thisset) # NameError: name 'thisset' is not defined
 """

""" LOOP SETS """

# for loop

thisset = {"Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"}
for x in thisset:
  print(x)