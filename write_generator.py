def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'

for i in simple_gen():
    print(i)

CORRECT_COMBO = (3, 6, 1)

'''
for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo: {}'.format((c1,c2,c3)))
                break
'''
def combo_gem():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

'''
instead of return things, it yields things in a stream
'''
for (c1, c2, c3) in combo_gem():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)
