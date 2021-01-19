# Dmitrii Dudchenko
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.
print("Сalculations of integers a and b")
a = int(input("Input int number a\n"))
b = int(input("Input int number b\n"))
s = a/b
t = a % b

print("answer with /", str(s))
print("answer with % -", str(t))


if a > b:
    print("answer a > b")
elif a == b:
    print("answer Equall")
else:
    print("answer b > a")
