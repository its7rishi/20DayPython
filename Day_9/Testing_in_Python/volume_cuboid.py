""" Python Unit Test """

# * unittest
# ? a testing framework for Python
""" 
  Features of unittest:
   ?  Test Automation
   ?  Sharing of setup and shut down code for test
   ?  Aggregating tests into collections
   ?  Independence of the tests from the reporting framework
 """

# Starting with Python unittest

# A function to calculate volume of a cube

def cuboid_volume(l):
  if type(l) not in [int, float]:
    raise TypeError("The length can only be a valid integer or float")
  return(l*l*l)

# length = [2,1.1, -2.5, 2j, 'two']

# for i in range(len(length)):
#   print(f"The volume of the cuboid: {cuboid_volume(length[i])}")
  