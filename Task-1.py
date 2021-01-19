# Dmitrii Dudchenko
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.
print("Сalculations of integers a and b")
a = input("Enter your name\n")
b = int(input("Input int number a\n"))
c = int(input("Input int number b\n"))
s = b / c
t = b % c

print(str(a),"answer with /", str(s))
print(str(a),"answer with % -", str(t))


if b > c:
    print(str(a),"answer a > b")
elif b == c:
    print(str(a),"answer Equall")
else:
    print("answer c > b")
