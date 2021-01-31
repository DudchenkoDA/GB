# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def users (*args):
    try:
        name = str(input("Enter name "))
        surname = str(input("Enter surname "))
        birthday = int(input("Enter birthday "))
        city = str(input("Enter city "))
        email = str(input("Enter email "))
        phone = int(input("Enter phone number "))
    except ValueError:
        return "Enter correct value data"

    return f"Name - {name}, Surname - {surname}, Birthday - {birthday}, City - {city}, Email - {email}, Phone - {phone}"
print(users())


