# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'
#
# for i in simple_gen():
#     print(i)

CORRECT_COMBO = (3, 6, 1)

# fount_combo = False
# for c1 in range(10):
#     if fount_combo:
#         break
#     for c2 in range(10):
#         if fount_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo: {}'.format((c1, c2, c3)))
#                 fount_combo = True
#                 break
#             print(c1, c2, c3)


def combo_gen():
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                yield (i1, i2, i3)

for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)
