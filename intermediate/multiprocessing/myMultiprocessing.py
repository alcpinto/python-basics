import multiprocessing


def spawn(num, num2):
    print('Spawned! {} {}'.format(num, num2))

if __name__ == '__main__':
    for i in range(5):
        # if we need to pass only 1 param we need to put a , in the end like
        # p = multiprocessing.Process(target=spawn, args=(i,))
        p = multiprocessing.Process(target=spawn, args=(i, i*2))
        p.start()
        # wait process finishes
        p.join()
