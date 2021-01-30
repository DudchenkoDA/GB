#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

my_month = int(input('Enter number of month (1 - 12)\n'))

month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
seasons = {1 :'Winter', 2 :'Spring', 3 :'Summer', 4 :'Outumn'}
if my_month in [1, 2, 12]:
    print("Season  -", seasons.get(1))
    print("Month - ", month[int(my_month-1)])
elif my_month in [3, 4, 5]:
    print("Season  -", seasons.get(2))
    print("Month - ", month[int(my_month-1)])
elif my_month == 6 or my_month == 7 or my_month == 8:
    print("Season  -", seasons.get(3))
    print("Month - ", month[int(my_month - 1)])
elif my_month == 9 or my_month == 10 or my_month == 11:
    print("Season  -", seasons.get(4))
    print("Month - ", month[int(my_month - 1)])
else:
    print("In this number no any month")