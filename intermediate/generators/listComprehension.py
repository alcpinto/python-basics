input_list = [5, 6, 2, 1, 6, 7, 10, 12]


def div_by_five(num):
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five(i))
# Same as
# xyz = []
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)

# for i in xyz:
#     print(i)
#
[print(i) for i in xyz]

xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)


[[print(i, ii) for ii in range(3)] for i in range(5)]
# for i in range(5):
#     for ii in range(3):
#         print(i, ii)

x = (print(i) for i in range(5))

for j in x:
    j




