""" ITERATORS """
# An iterator is an object that contains a countable number of values  
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator Vs Iterables

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.  
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))   

# Strings are also iterable objects, and can return an iterator:
mystr = "banana"

myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) 

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

  # The for loop actually creates an iterator object and executes the next() method for each loop.
# This is why we can use the break statement to stop the loop when we want to.

# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# In this example, we create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1, 2, 3, 4, etc.):
""" 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x
  

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
 """
# Stop Iteration

# The example above would continue forever if you had enough next() statements, or if it were used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error  if the iteration is done a specified number of times:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
    print(x)