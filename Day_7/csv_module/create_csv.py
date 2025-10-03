import csv

headings = ["Name", "Age", "City", "Country", "Phone"]

row_data = [
  ["Jack", 33, "Lisbon", "Portugal", "+23 1928392829"],
  ["Mike", 23, "Istanbul", "Turkey", "+12 3283720482"],
  ["Mila", 19, "Edinburgh", "Scotland", "+12 9283923722"],
  ["Shilpa", 39,"Bhopal", "India", "+91 9283728421"]
]

file_name = "sales_reps.csv"
file_location = "/Users/saptarshimajumdar/20DayPython/Day_7/csv_module/" + file_name

with open(file_location, 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile)

  csvwriter.writerow(headings)

  csvwriter.writerows(row_data)