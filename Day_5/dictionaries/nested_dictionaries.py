""" NESTED DICTIONARIES """

# dictionaries can be nested

myFamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}

# print(myFamily)

# * You can also add multiple dictionaries into a single dictionary

car = {
  "brand": "Ford",
  "model": "Fiesta"
}

bike = {
  "brand": "Triumph",
  "model": "Thunderbird"
}

bicycle= {
  "brand": "Firefox",
  "model": "XVZ"
}

myWheels = {
  "car": car,
  "bike": bike,
  "bicycle": bicycle
}

# print(myWheels)

# * Access Items Nested Dictionaries

# print(myWheels["bike"] ["brand"])

# * Loop through nested dictionaries

for x, obj in myWheels.items():
  print(x)

  for y in obj:
    print(y + ': ', obj[y])