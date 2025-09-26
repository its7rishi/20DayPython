def counter():
  word_count = {}

  user_input = input("Enter a few words: ")

  clean_words = ""

  for char in user_input.lower():
    if 'a' <= char <= 'z' or '0' <= char <= '9' or char == ' ':
      clean_words += char
    else:
      clean_words += ' '
  
  words = clean_words.split()

  for word in words:
    if word:
      if word in word_count:
        word_count[word] += 1
      else:
        word_count[word] = 1
  return word_count

print(counter())