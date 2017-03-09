import matplotlib.pyplot as plt


def graph_operation(x, y):
    print('function that graphs {} and {}'.format(x, y))
    plt.plot(x, y)
    plt.show()

x = [1, 2, 3]
y = [2, 3, 1]

graph_me = [x, y]

graph_operation(*graph_me)
