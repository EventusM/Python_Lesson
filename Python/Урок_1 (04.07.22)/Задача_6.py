km_1 = float(input('Сколько километров спортсмен пробежал в первый день? '))
finish = float(input('Желаемый результат? '))
km_sum = 0
day_1 = 1
while True:
    if km_1 <= 0 or finish <= 0:
        print('Результата не получится. увы... выхода нет.')
        break
    elif km_1 >= finish:
        print('Поздравляю вы уже всего достигли!')
        break
    while km_1 < finish + km_1:
        print(f'{day_1}-й день {km_1:.02f} км.')
        if km_1 < finish:
            km_sum = km_1 * 0.1
            km_1 = km_1 + km_sum
            day_1 += 1
        else:
            print(f'На {day_1}-й день спортсмен достигнет - около {km_1:.0f} км.')
            break
    break

