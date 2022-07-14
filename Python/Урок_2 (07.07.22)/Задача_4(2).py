list = input('введите слово - ').split()
for i, v in enumerate(list, 1):
    print(f'{i}) {v:.10}')