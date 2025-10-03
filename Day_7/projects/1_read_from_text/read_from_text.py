""" 
TXT WORD COUNTER
________________

This program :
1. reads text from a txt file.

2. counts the occurrence of each word

3. exports the count to a csv file

 """

def counter():

  # A dictionary that'll store words as keys and count as value
  word_count = {}

  # read the txt file at the specified location
  with open('/Users/saptarshimajumdar/20DayPython/Day_7/projects/1_read_from_text/passage.txt') as passage:

    text = ""
    
    # assign the text variable with the contents of the txt file
    for x in passage:
      text += x

    # a variable to store the text after removing special characters
    clean_words = ""

    # converting text to lower case and adding characters to clean_words variable. # The special characters are filtered out.
    for char in text.lower():
      if 'a' <= char <= 'z' or '0' <= char <= '9' or char == " ":
        clean_words += char
      else:
        char += " "
    
    # Splitting the text in clean_words into an list
    # Each word will be a list element
    words = clean_words.split(" ")

    # Check if the word is present in the word_count dictionary
    # if present increase the count else set the count as 1
    for word in words:
      if word in word_count:
        word_count[word] += 1
      else:
        word_count[word] = 1
    
    # send word_count to to export_to_csv funtion
    export_to_csv(word_count)
  

def export_to_csv(count):
  import csv # import csv module

  headers = ['word', 'count'] # define the headers of the csv file
  rows = [] # to store the row data

  for x in count:
    if not x == '':
      # convert each key value into an array element and append to row variable
      rows += [[x, count[x]]]

  # Create the csv file
  # provide the location
  with open('/Users/saptarshimajumdar/20DayPython/Day_7/projects/1_read_from_text/word_count.csv', 'w', newline='') as csvfile:

    # create a writer object of csvfile
    writer = csv.writer(csvfile)

    # write the header row
    writer.writerow(headers)

    # write the data rows
    writer.writerows(rows)
  
counter()