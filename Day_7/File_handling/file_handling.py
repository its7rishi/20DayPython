""" FILE HANDLING """

# * open() function
# ? takes two parameters; filename, mode
# ? There are four different modes  for opening a file.
# ? 'r' - read (default) - opens a file for reading, error if the file does not exist
# ? 'a' - append - opens a file for appending, creates the file if it does not exist
# ? 'w' - write - opens a file for writing, creates the file if it does not exist
# ? 'x' - create - creates the specified file, returns an error if the file exists

# ? In Addition we can specify if the file should be handled as binary or text mode
# ? 't' - text (default) - text mode
# ? 'b' - binary - binary mode (e.g. images)

# Syntax
# f = open("demofile.txt")

# ? the code is same as :

# f = open("demofile.txt", "rt")

# ? r - read and t - text are default values, so we do not need to specify them
# ! Make sure the file exists, or else it will raise an error

# f = open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt")
# print(f.read())

# with statement
# ? it is used to open a file and close it automatically after the nested block of code
# with open("demofile.txt") as f:
#     print(f.read()) # ? no need to use f.close()  here
""" 
with open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt") as f:
  print(f.read())
   """

# * Close File
# ? It is a good practice to close the file when you are done with it.
# ? if not using a with statement, you must write a close statement to close the file
""" 
f = open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt")
print(f.readline())
f.close()
 """

# * Read only parts of the file
""" 
with open('/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt')  as f:
  # print(f.read(5)) # reads the first 5 characters of the file
  print(f.readline()) # reads one line of the file
  print(f.readline()) # calling it twice, you read two lines of the file  

 """  # ? By looping through the lines of the file, you can read the file line by line

with open('/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt') as f:
  for x in f:
    print(x)
