# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        arg1 = int(input("Enter int number arg1"))
        arg2 = int(input("Enter int number arg2"))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Error: Zerro no division number"
    except ValueError:
        return "Error: You need enter int number"

    return f"arg1 / arg2 = {res}"


print(div())
