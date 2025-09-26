""" REMOVE ITEMS """

person = {
  "name": "Peter",
  "age": 33,
  "gender": "male",
  "height_cms": 189,
  "hair": "blond",
  "build": "muscular",
  "weight_kgs": 89,
  "city": "Lisbon",
  "country": "Portugal",
  "married": True,
  "no_of_children": 2
}

print(person)

# pop() method
#? Removes values with specified key name
""" 
person.pop("no_of_children")
print(person)
 """

# pop_item()
# ? removes the last inserted item
# ! In versions prior to 3.7, random item is removed instead

person.popitem()
# print(person)

# * del keyword
# ? removes the item with specified keyword

del person["age"]
# print(person)

# ! del keyword can also delete the dictionary completely
""" 
del person
print(person) # NameError: name 'person' is not defined
 """

# clear() method
# ? Empties the dictionary

person.clear()
print(person)
