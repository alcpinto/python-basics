for i in range(4):
    print(i)

# Code similar to the block bellow. Generates a list
xyz = [i for i in range(5)]

print(xyz)

# Code similar to the block above
xyz = []
for i in range(5):
    xyz.append(i)

print(xyz)


# With parentheses is only a generator and do not store values in memory
xyz = (i for i in range(5))

print(xyz)

for i in xyz:
    print(i)
