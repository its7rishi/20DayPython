# * LOOP LISTS


thisList = ['apple', 'banana', 'cherry']

# for loop

for x in thisList:
  print(x)


# * Loop through index numbers

# range()

for i in range(len(thisList)):
  print(thisList[i])


# while loop

i = 0
while i < len(thisList):
  print(thisList[i])
  i += 1

# * LOOPING USING LIST COMPREHENSION

names = ['Jerry', 'Tom', 'Spike', 'Tike']
[print(x) for x in names]