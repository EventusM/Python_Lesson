while True:
    km_1 = float(input('Сколько километров спортсмен пробежал в первый день? '))
    finish = float(input('Желаемый результат? '))
    if km_1 <= 0 or finish <= 0 or km_1 > finish:
        print('Результата не получится.')
        break
    km_sum = 0
    day_1 = 1
    while True:
        print(f'{day_1}-й день {km_1:.02f} км.')
        if km_1 <= finish:
            km_sum = km_1 * 0.1
            km_1 = km_1 + km_sum
            day_1 += 1
        else:
            print(f'На {day_1}-й день спортсмен достигнет результата - около {km_1:.0f}.км.')
            break



