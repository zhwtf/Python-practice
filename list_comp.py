input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

print(xyz)

for i in xyz:
    print(i)

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
