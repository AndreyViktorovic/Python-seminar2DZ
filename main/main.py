#n = input('Введите 3-х значное число: ')
#res = 0
#if len(n) == 3:
#    for i in n:
#        res += int(i)
#    print(res)
#else:
#    print('Вы ввели не 3-х значное число')

#Task 2

#n = int(input('введите сколько сделали журавликов Петя Катя и Сережа : '))
#petr = n / 6  #количество журавликов сделаных Петей
#sergey = petr  # количество журавликов сделаных Сережой
#ekaterina = (sergey + petr) * 2 # количество журавликов сделаных Катей
#print(int(sergey), int(ekaterina), int(petr))

# Taks 3

#n = input('Введите шестизначный номер билета общественного транспорта: ') #Ввод начальных данных
#l = int(n[0]) + int(n[1]) + int(n[2])  #Проверка первого условия, сумма первых трех цифр
#r = int(n[3]) + int(n[4]) + int(n[5])  #Проверка второго условия, сумма вторых трех цифр
#if l == r:  # Проверка третьего условия, равенство первого и второго условия
#    print('Yes')  # печть результата
#else:
#    print('NO')

# Taks 4

a = int(input('Введите ширину шоколадки: ')) #Ввод начальных данных
b = int(input('Введите длину шоколадки: ')) #Ввод начальных данных
c = int(input('Введите количество долек шоколадки: ')) #Ввод начальных данных
if a*b<c or c==a*b:
    print ('NO')
elif c%b==0 or c%a==0:
    print ('YES')
else: 
    print ('NO')