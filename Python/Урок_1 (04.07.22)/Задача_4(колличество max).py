
numbers = int(input('Введите целое положительное число: '))
max_num = 0
ost_num = numbers
kol_num = 0
while ost_num > 0:
    ost = ost_num % 10
    if ost > max_num:
        max_num = ost
    ost_num = ost_num // 10
a = numbers
while a > 0:
    b = a % 10
    if b == max_num:
        kol_num += 1
    a = a // 10
print(f'Наибольшая цифра в числе - {numbers} \nРавна - {max_num} \nКолличество максимальный чисел - {kol_num}\n')






