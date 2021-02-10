# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


# my_f = open("text.txt", 'w')
# i = 1
# while i <= 10:
#     str_line = my_f.write(input("Enter line\n"))
#     i += 1
#     my_f = open("text.txt", "r")
#     print(my_f)
# my_f.close()


with open('text.txt', 'w', encoding = 'utf-8') as my_f:
    while(text := input('Enter text line, when no simvol it stop\n')) != '':
        print(text, file=my_f)