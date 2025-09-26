""" COPY DICTIONARY """

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# copy() method
#? makes a copy of a dictionary

newDict = thisdict.copy()
print(newDict)

# use the dict() function

myCar = dict(thisdict)
print(myCar)