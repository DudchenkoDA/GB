#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

words = str(input('Enter few words with space\n'))

for num, new_line in enumerate(words.split(), start=1):
    print(num, new_line[0:10])