""" LOOP DICTIONARY """

house = {
  "category": "apartment",
  "area_sqft": 2000,
  "type": "3BHK",
  "bathrooms": 2,
  "furnished": False,
  "vaastu_complaint": True,
  "city": "Mumbai",
  "state": "Maharashtra",
  "area": "Bandra",
  "price": 30000000
}

# print all key names
""" 
for x in house:
  print(x)
 """
# print all values
""" 
for x in house:
  print(house[x])
 """
# values() method
# ? returns all the values of the dictionary
""" 
values = house.values()

print(values)
 """

# * Print all keys
# keys() method
# ? returns all the keys in the dictionary
""" 
keys = house.keys()
print(keys)
 """

# * LOOP THROUGH KEYS & ITEMS
# items() method

for x, y in house.items():
  print(x,y)
