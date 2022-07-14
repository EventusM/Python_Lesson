list = [1, 2.2, (-3 + 3j), None, True, [4, 4], (6, 6.6),
        {7: 'seven', 8: 'eight'}, {9, 10}, range(11),
        frozenset(), bytearray(b'ten'), b'one',
        zip(*[(12, 13), ('q', 'w')]), TypeError]
for i, val in enumerate(list, 1):
    print(f'{i}) {val} - {type(val)}')