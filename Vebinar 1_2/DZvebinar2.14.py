# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


n = int(input('Введите число N: '))
k = 0
res = 1
while res < n+1:
    print(res, end=' ')
    k += 1
    res = 2 ** k