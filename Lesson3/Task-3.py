# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func (*args):
    arg1 = int(input("Input number arg1 - "))
    arg2 = int(input("Input number arg2 - "))
    arg3 = int(input("Input number arg3 - "))
    args = [arg1, arg2, arg3]
    max1, max2 = args[0], None
    for a in args[1:]:
        if a > max1:
            max1, max2 = a, max1
        elif max2 == None or a > max2:
            max2 = a
    return (max1, max2)

print(sum(my_func()))



