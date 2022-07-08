sekond_o = int(input('Bведите секунды: '))
minutes_sum = sekond_o // 60
sekonds = sekond_o - (minutes_sum * 60)
hour = minutes_sum // 60
minutes = minutes_sum - (hour * 60)
print(f'{hour:02}:{minutes:02}:{sekonds:02}')
