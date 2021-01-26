#2. Для списка реализовать обмен значений соседних элементов, т.е.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().


index_count = int(input("Enter count index of list"))
my_list = []
index = 1
i = 0
while index <= index_count:
    my_list.append(input('Enter value of list - '))
    index += 1
print(my_list)
for change_list in range(int(len(my_list)/2)):
   my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
   i += 2
print(my_list)