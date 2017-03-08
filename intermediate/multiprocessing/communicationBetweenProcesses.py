from multiprocessing import Pool


def job(num):
    return num * 2

if __name__ == '__main__':
    pool = Pool(processes=20)
    data = pool.map(job, range(40))
    data2 = pool.map(job, [2, 5])
    pool.close()
    print(data)
    print(data2)

