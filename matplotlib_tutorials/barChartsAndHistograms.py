import matplotlib.pyplot as plt

# x = [1, 3, 5, 7, 9]
# y = [5, 2, 7, 8, 2]
#
# x2 = [2, 4, 6, 8, 10]
# y2 = [8, 6, 2, 5, 6]
#
# plt.bar(x, y, label='Bars 1')
# plt.bar(x2, y2, label='Bars 2')
#
#
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('My bar graph')
# plt.legend()
#
# plt.show()

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130,
                   111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
# plt.legend()
plt.show()
