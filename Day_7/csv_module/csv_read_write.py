import csv

# Opening a csv file
""" 
with open("/Users/saptarshimajumdar/20DayPython/Day_7/csv_module/users.csv") as file:
  csvFile = csv.reader(file)


  for line in csvFile:
    print(line)

 """

# Creating a CSV File
# fieldnames
f = ["Name", "Branch","Year", "CGPA"]

# Data rows for the csv file
r = [
  ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

# name of the csv file
fn = "university_records.csv"

# writing to the csv file
with open(fn, 'w', newline='') as csvfile:
  cswriter = csv.writer(csvfile)

  # Writing the field names
  cswriter.writerow(f)

  # Writing the data rows
  cswriter.writerows(r)