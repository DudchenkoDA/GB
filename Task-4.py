# Dmitrii Dudchenko
# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
a = int(input("Enter number more 9\n"))
ab = []
while a > 10:
    ab.append(a % 10)
    a //= 10
c = max(ab)

print(c)

