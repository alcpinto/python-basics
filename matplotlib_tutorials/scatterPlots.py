import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

plt.scatter(x, y, label='my legend', marker='*')

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('''
My scatter plot
Check it out''')
plt.legend()

plt.show()

