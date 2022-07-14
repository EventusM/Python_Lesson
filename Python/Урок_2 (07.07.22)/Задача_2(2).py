list = input("Введите число -  ").split()
for i in range(1, len(list) // 2,2):
    list[1 - 1], list[1] = list[i], list[i - 1]

print(list)