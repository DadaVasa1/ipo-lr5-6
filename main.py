# Считываем имя файла от пользователя
filename = input("Введите имя файла: ")

# Открываем файл в режиме чтения
with open(filename, 'r') as file:
  # Считываем текст из файла
  text = file.read()
  # Разделяем текст по пробелам
  words = text.split()
  # Подсчитываем количество слов
  word_count = len(words)

# Выводим результат
print(f"В файле '{filename}' {word_count} слов.")