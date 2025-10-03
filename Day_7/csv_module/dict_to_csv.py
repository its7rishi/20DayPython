import csv

# dictionary data
my_data = [
  {"id": 1, "brand": "Ferrari", "model": "F50 Spyder", "color": "red", "year": 1978},
  {"id": 2, "brand": "Porsche", "model": "911", "color": "black", "year": 1998},
  {"id": 3, "brand": "Lamborghini", "model": "Diablo", "color": "yellow", "year": 1999},
  {"id": 4, "brand": "Lotus", "model": "Elise", "color": "blue", "year": 200},
]

# Column Headers
headings = ['id', 'brand', 'model', 'color', 'year']

# file name
file_name = 'my_cars.csv'

# path of csv file
file_path = "/Users/saptarshimajumdar/20DayPython/Day_7/csv_module/" + file_name

# Writing to csv file
with open(file_path, 'w', newline="") as csv_file:
  # creating a csv DictWriter object
  writer = csv.DictWriter(csv_file, fieldnames=headings)

  # writing the headers
  writer.writeheader()

  # writing the data rows
  writer.writerows(my_data)

with open(file_path) as file:

  for line in file:
    print(line)

  
