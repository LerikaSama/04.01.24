#Заадание 1
#
#diap = int(input("Введите начало диапазона для поиска простых чисел: "))
#diapk = int(input("Введите конец диапазона для поиска простых чисел: "))
#for num in range(diap, diapk):
#    a = 0
#    b = 2
#    while b < num:
#        if num % b == 0:
#            a += 1
#        b += 1
#    if a == 0:
#        print(f'{num} простое число')


#Задание 2

#for i in range(1,10):
#    for j in range(1,10):
#        print("%4d" % (i*j), end='')
#    print()

#Задание 3

for i in range(int(input('введите начало: ')),int(input('введите конец: '))+1):

   print()

   for j in range(1,11):

       print(f'{i}*{j}={i*j}',end=' ')