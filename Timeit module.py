import timeit

input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

#create a generator is faster than list
#generator
xyz = (i for i in input_list if div_by_five(i))

#list
xyz = [i for i in input_list if div_by_five(i)]

print(timeit.timeit('''
nput_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i)''', number=5000))
