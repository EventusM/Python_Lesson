numbers = int(input('Введите целое положительное число: '))
max_num = 0
ost_num = numbers
while ost_num > 0:
    ost = ost_num % 10
    if ost > max_num:
        max_num = ost
        if max_num == 9:
            break
    ost_num = ost_num // 10
print(f'Наибольшая цифра в числе - {numbers} \nРавна - {max_num} \n')

