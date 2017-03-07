import timeit

# input_list = range(100)
#
#
# def div_by_five(num):
#     return num % 5 == 0
#
# # generator, converted to list.
# xyz = (i for i in input_list if div_by_five(i))


print(timeit.timeit('''
input_list = range(100)


def div_by_five(num):
    return num % 5 == 0

# generator, converted to list.
xyz = list(i for i in input_list if div_by_five(i))
''', number=5000))
