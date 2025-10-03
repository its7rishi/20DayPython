""" WRITE OR CREATE FILE """

# ? To write to an existing file, you need to add a parameter to  open() function
# ? "a" = Append - will append to the end of file.
# ? "2" = Write = Will overwrite any content in the file
""" 
with open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt", "a") as f:
  f.write("Now the file has more content!")

  with open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt") as f:
    print(f.read())

 """

# * Overwrite existing content
# use the "w" parameter
""" 
with open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content")

with open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt") as f:
  print(f.read())
 """

# * CREATE A FILE
""" 
Use one of the following parameters

'x' = creates a file. throws an error if the file already exists
'a' = will create the specified file if it does not exist
'w' = will create the file if the specified file does not exist
 """
""" 
f = open("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/myfile.txt", "x") # A new file gets created. Throws an error if the file already exists

 """

# * DELETE A FILE

# ? To delete a file, you need to import the os module
""" 
import os
os.remove('/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt')
 """

# Check if file exists
""" 
import os
if os.path.exists("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt"):
  os.remove("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/demofile.txt")
else:
  print("The file does not exist")
 """


# * DELETE FOLDER
# ? use the os.rmdir() method
# ! YOU CAN ONLY REMOVE EMPTY FOLDERS

import os
os.rmdir("/Users/saptarshimajumdar/20DayPython/Day_7/File_handling/my_folder")
