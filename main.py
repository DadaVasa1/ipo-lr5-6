filename = 'text.txt'

with open(filename) as file:
  text = file.read()
  words = text.split()
  countword = len(words)
  print("В файле text.txt", countword, "слова.")
