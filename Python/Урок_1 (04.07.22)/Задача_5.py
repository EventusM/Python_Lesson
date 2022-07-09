profit = float(input('Какая выручка?: '))
lesion = float(input('Сколько издержек?: '))
net_profit = profit - lesion
if net_profit > 0:
    print(f'Чистая прибыль = {net_profit}руб.\nПоложительный финансовый результат :) \n')
    employee = int(input('Количество сотрудников?: '))
    print(f'Прибыль на одного сотрудника = {net_profit / employee:.2f}руб.\n'
          f'Рентабельность компании = {(net_profit / lesion) * 100:.1f}%.')
elif net_profit < 0:
    print(f'Чистая прибыль = {net_profit}руб.\n'
          f'Отрицательный финансовый результат :(\n')
else:
    print(f'Чистая прибыль = {net_profit}руб.\n'
          f'Отсутствует прибыль :| \n')

