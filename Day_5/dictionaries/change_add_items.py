""" CHANGE ITEMS """

# Change Values

bike = {
  "brand": "Royal Enfield",
  "model": "Thunderbird",
  "year": 2009,
  "color": "black",
  "power": "350cc"
}

bike["color"] = "red"
# print(bike["color"])

# * Update Dictionary

# update() method
# ? updates the dictionary with the item from given argument

bike.update({"year": 2010})
# print(bike["year"])

# * ADD ITEM

bike["front_brake"] = "disc"
bike["rear_brake"] = "drum"

# update() method
# ? update() method can also be used to add an item in the dictionary

bike.update({"transmission": "MT"})
print(bike)


