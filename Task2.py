# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def list_by_user(string):
    print(string)
    len = int(input("Сколько будет элементов в списке? "))
    list = []
    for i in range(len):
        a = int(input("Введите число в список: "))
        list.append(a)
    return list


lst = list_by_user("Задайте список из целых чисел.")
print(lst)
sum_list = []
if(len(lst)%2 == 0):
    for j in range(len(lst)//2):
        s = lst[j] * lst[-j-1]
        sum_list.append(s)
else:
    for j in range(len(lst)//2+1):
        s = lst[j] * lst[-j-1]
        sum_list.append(s)    
print(sum_list)
