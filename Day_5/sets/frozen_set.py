""" FROZEN SET 🥶  """

#? frozen set is an immutable version of set
#? Contains unique, unordered, unchangeable elements
#? Elements cannot be added or removed from the frozen set

# use frozenset() constructor to create frozen set

# my_set = frozenset({"apple", "banana", "cherry"})
""" 
print(my_set)
print(type(my_set))
 """

# * Methods
# copy()
# ? Creates a shallow copy
""" 
copy_set = my_set.copy()

print(copy_set)
print(type(copy_set))
 """

# * difference()

set1 = {"apple", "banana", "cherry"}
set2 = {"guava", "cherry", "orange"}
""" 
new_set = set1.difference(set2)
print(new_set)
 """

# * intersection()

new_set = set1.intersection(set2)
print(new_set)
print(type(new_set))