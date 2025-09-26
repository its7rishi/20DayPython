# Sort Lists

""" 
fruits = ['orange', 'mango', 'kiwi', 'banana', 'apple']
nums = [3, 2, 9, 4, 1, 7, 21, 11]

# * sort() method

fruits.sort()
nums.sort()
print(fruits)
print(nums)

# * Reverse Sort
# reverse = True argument

fruits.sort(reverse=True)
nums.sort(reverse=True)

print(fruits)
print(nums)
 """

# * CUSTOMIZE SORT FUNCTION

# ? Below program sorts the list based on how close a number is to 50
""" 
def myFunc(n):
  return abs(n-50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myFunc)
print(thisList) # Output - [50, 65, 23, 82, 100]
 """

# * CASE INSENSITIVE SORT
# sort() by default is case sensitive
# capital letters are sorted before lower case letters
""" 
alphas = ['a', 'b', 'C', 'D', 'e', 'f', 'g', 'h']
alphas.sort()
print(alphas)   # Output = ['C', 'D', 'a', 'b', 'e', 'f', 'g', 'h']

# ? use str.lower key function to make case-insensitive sort
alphas.sort(key=str.lower)
print(alphas) # Output - ['a', 'b', 'C', 'D', 'e', 'f', 'g', 'h']
 """

# * REVERSE THE ORDER
# ? Reverse the order of a list regardless of the alphabet

fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.reverse()
print(fruits)