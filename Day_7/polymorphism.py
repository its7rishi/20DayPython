""" POLYMORPHISM """

# ? means 'many forms'
# ? in programming, it refers to methods/functions/operators with the same name that can be executed in many objects or classes.

# * FUNCTION POLYMORPHISM
# An example of polymorphism that can be used on different objects is the len() function.

# Examples -
""" 
print(len("Hello"))  # Output: 5

my_tuple = ("apple", "banana", "cherry")
print(len(my_tuple))  # Output: 3

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print

# * CLASS POLYMORPHISM
# Polymorphism is often used in class methods, where we can have multiple classes with the same method name.

# Example -

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive")


class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly")   
  

car1 = Car("Ford", "Mustang")
boat1 = Boat("Yamaha", "212X")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  x.move()  # Output: Drive Sail Fly
 """

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail")

class Plane(Vehicle):
  def move(self):
    print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Yamaha", "212X")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()