#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.

#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


rating = [8, 4, 6, 5, 7, 1, 7]
print(sorted(rating, reverse = True))

number = int(input('Enter number of rating - '))
if number > 0 or number < 10:
    rating.append(number)
    print(sorted(rating, reverse = True))
#   else:
#   print("Number not in 0-10")
print("\nSecond type of decision\n")


while True:
    word = input('Enter number of rating (or empty string to exit) - ')
    if word == '':
        break
    if word != int:
        print("Enter need to use type int")
    number = int(word)
    if number > 0 or number < 10:
        rating.append(number)
        print(sorted(rating, reverse = True))