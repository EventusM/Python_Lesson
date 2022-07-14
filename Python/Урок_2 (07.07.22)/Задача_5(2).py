list = [8, 7, 5, 3, 3, 3, 2, 8, 7, 5, 3, 3, 2]
new_number = ''
while new_number != 'q':
    i = 0
    new_number = input('Введите натуральное число.\n выход - q\n')

    if new_number.isdigit():
        for n in list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        list.insert(i, int(new_number))
    print(list)
