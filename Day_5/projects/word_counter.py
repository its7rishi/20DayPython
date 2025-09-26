def frequency_counter():
  str_input = input("Please enter a few words: ")

  return f"Word count: {len(str_input.split())} \n Characters: {len(str_input)}"

  


print(frequency_counter())