""" JOIN SETS """
# * UNION
# union() method
""" 
set1 = {"A", "B", "C"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# | operator

set4 = set1 | set2
print(set4)
 """

# * JOIN MULTIPLE SETS
""" 
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
set3 = {'!', '$', '@'}

# with union() method
set4 = set1.union(set2, set3)
print(set4)

# with | operator
set5 = set1 | set2 | set3
print(set5)
 """
# * JOIN a Set and a Tuple

# ? NOTE: The '|' operator only allows you to join sets with sets

# join() method
""" 
set1 = {"apple", "banana", "cherry"}
tuple1 = ("peach", "grapes", "orange")
set2 = set1.union(tuple1)
print(set2)
 """

# * UPDATE

# update() method

#? Inserts all items from one set to another
#? Changes the original set and does not return a new set
""" 
set1 = {1, 2, 3}
set2 = {"I", "II", "III"}

set1.update(set2)
print(set1)
 """

# ? Both union() and update() remove duplicate items 
""" 
fruits = {"apple", "banana"}
fruits2 = {"banana", "cherry"}

# result = fruits.union(fruits2)
# print(result)
fruits.update(fruits2)
print(fruits)
 """

""" INTERSECTION """
# intersection() method
# ? returns a new set that contains only items present in both the sets
# ? Allows to join sets with other iterables
""" 
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "mango"}

set3 = set1.intersection(set2)
print(set3)

# '&' operator
# ? Only allows to join sets with sets.
set4 = set1 & set2
print(set4)
 """
# intersection_update() method
# ? keeps only duplicate values
# ? Does not return a new set, updates the original set
""" 
brands = {"Dell", "HP", "Asus"}
brands_2 = {"Lenovo", "HP", "Microsoft", "Asus"}
# brands_3 = {"Dell" "Asus", "HP"}

brands.intersection_update(brands_2)
print(brands)
 """

# ? True, False, 1 and 0 are considered as duplicates
""" 
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google",1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)
 """

# * DIFFERENCE
# difference() method
# ? returns only items from the first set that are not present in the other set

set1 = {"apple", "banana", "cherry"}
set2 = {"guava", "apple", "apricot"}
""" 
set3 = set1.difference(set2)

# ? You can also use ' - ' operator to get the same result
# ? The ' - ' operator only allows to join sets to sets
set4 = set1 - set2

print(set3)
print(set4)
 """

# difference_update() method
# ? Does not return a new set, changes the original set
""" 
set1.difference_update(set2)
print(set1)
 """

# symmetric_difference() method
# ? keeps only elements that are not present in both sets
""" 
unique = set1.symmetric_difference(set2)
print(unique)
 """
# ? Using the ' ^ ' operator gives the same result
# ? THE ' ^ ' operator only allows to join sets to sets
""" 
unique2 = set1 ^ set2
print(unique2)
 """

# * symmetric_difference_update() method
# ? Does not return a new set, It modifies the original set

set1.symmetric_difference_update(set2)
print(set1)