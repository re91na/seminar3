# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n10 = int(input("Введите любое целое число "))
o = n10
n2 = ""
while o > 0:
    n2 = str(o % 2) + n2
    o = o // 2
print(f"Десятичное число {n10} в двоичной системе будет выглядеть как {n2}")