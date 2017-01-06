xyz = [i for i in range(5)]
print(xyz)
#generator---the list is not stored in memory
xyz = (i for i in range(5))
print(xyz)

for i in xyz:
    print(i)
