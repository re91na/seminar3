# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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
sum = 0
for j in range(0, len(lst)):
    if (j % 2 != 0):
        sum += lst[j]
print(sum)
