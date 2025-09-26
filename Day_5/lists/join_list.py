# JOIN LISTS

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# * + operator

join1 = list1 + list2
print(join1)

# * Join one by one using append

for x in list2:
  list1.append(x)

print(list1)

# * extend() method

list1.extend(list2)
print(list1)