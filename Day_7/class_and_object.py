""" CLASSES / OBJECTS """

# * CLASS
# ? It is an object constructor like a 'blueprint' for creating objects

# To create class use the keyword ' class '
""" 
class MyClass:
  x = 5
 """

# * __init__() method
# ? All classes have a method called __init__()
# ? it is always executed when the class is created
# ? Use the __init__() method to assign values to object properties or other operations that are necessary to do when the object is being created
# ? The __init__() is called automatically every time the class is being used to create a new object
""" 
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 18)

print(p1.name, p1.age)
"""    

# * The __str__() method
# ? it controls what should be returned when the class object is represented as a string.

# ? If the __str__() method is not set, the string is a representation of the object itself
""" 
class Person:
  def __init__(self, name , age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"{self.name} {self.age}"

p1 = Person("Will", 33) 

# Without __str__() method 
# print(p1) # <__main__.Person object at 0x1013d6840>

# with __str__() method
print(p1) # will 33
 """

# * You can create your own method inside a class

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def greet(self):
    return f"Hi!, my name is {self.name}, I am {self.age} years old."
  
""" 
p1 = Person("Peter", "22")

print(p1.greet())
 """
# ? 'self' parameter is a reference to the current instance of the class
# ? it is used to access variables that belong to the class
# ? it need not be named 'self', you can name it anything you want
""" 
class Car:
  def __init__(content, brand, model, year, color):
    content.brand = brand
    content.model = model
    content.year = year
    content.color = color

  def intro(content):
    return f" A {content.color} {content.brand} {content.model}, {content.year}"
  

my_car = Car('Ford', 'Endeavour', '2023', 'black')

my_car.color = 'white'

# DELETE OBJECT
# user the del keyword

# del my_car

print(my_car.intro())
 """

# * INHERITANCE

# ? allows us to define a class that inherits methods and properties from another class
# ? Parent Class - The class that is being inherited from
# ? Child Class - The class that inherits from the parent class. Also called derived class.

# * Create a parent class
# Syntax is same as creating any other class

class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def print_name(self):
    print(self.fname, self.lname)

# * Create a child class
""" 
class Student(Person):
  pass
 """

# ? use pass if you do not want to add any other properties
""" 
x = Student('Harry', 'Potter')

x.print_name()
 """

# * Adding the __init__() function to the child class
# * When you add __init__() to the child class, it will no longer inherit the parent's __init__() function as it over-rides the parent's __init__() function

#? To keep the parent's __init__() function, you must add a call to the parent's __init__() function
""" 
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


x = Student("Ramesh", "Das")

x.print_name()
 """

# * super() function
# ? It makes the child class inherit all the methods and properties from the parent class.
# ! No need to use the name of the parent element. It sill automatically inherit all the properties and methods from the parent element

class Employee(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

e = Employee('Mark', 'Jonas', 2020)

e.welcome()