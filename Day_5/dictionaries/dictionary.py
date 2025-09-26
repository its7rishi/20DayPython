""" DICTIONARIES """
# * Dictionary
# ? Used to store data in key-value pairs
#? It is a collection datatype which is ordered, changeable and do not allow duplicates
#? Duplicate values are over-written
#? Can hold multiple data types
""" 
mydict = {
  "name": "Jake",
  "age": 44,
  "city": "Mumbai",
  "married": False,
  "colors": ['red', 'white', 'green'],
  "height_in_feet": 5.4
}

print(mydict)
print(type(mydict))
print(mydict["city"])
print(len(mydict))
 """

# * dictionary constructor
# use the dict() method to createa dictionary
""" 
person = dict(name = "John", age= 44, married = True, city = "Mumbai")

print(person)
print(type(person))
 """

# * Access Items
car = {
  "brand": "Toyota",
  "model": "Innova",
  "year": 2024,
  "color": "red",
  "transmission": "AT"
}
""" 
model = car["model"]
print(model)
 """
# get() method
""" 
x =car.get('brand')
print(x)
 """
# * Get Keys

# keys() method
""" 
car_keys = car.keys()
print(car_keys)

car["bhp"] = 3000
print(car_keys)
 """
# * Get Values

# values() method
""" 
value = car.values()
print(value)
 """
# * Get Items

# items() method
# ? Returns each item in the dictionary as a tuple in a list
""" 
car_items = car.items()
print(car_items)
 """

# * CHECK IF KEY EXISTS

if "model" in car:
  print("Yes, \"model\" is a key in the car dictionary")