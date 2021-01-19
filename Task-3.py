# Dmitrii Dudchenko
# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369


n = int(input("Enter  number n:\n"))
number = str(n)
nn = number + number
nnn = nn + number
sum = n + int(nn) + int(nnn)
print(f"Entered number in n + nn + nnn ={sum}\n")
print("Entered number in exponentiation by 3 =", n**3)