
# import os
#
# curDir = os.getcwd()
# print(curDir)
#
#
# os.mkdir('newDir')
#
# import time
#
# time.sleep(2)
# os.rename('newDir', 'newDir2')
#
# time.sleep(2)
# os.rmdir('newDir2')


import sys

# sys.stderr.write('This is a stderr text\n')
# sys.stderr.flush()

# sys.stdout.write('This is a stdout text\n')
# sys.stdout.flush()

# print(sys.argv)

if len(sys.argv) > 1:
    print(float(sys.argv[1]) + 5)


def main(arg):
    print(arg)

if __name__ == '__main__':
    main(sys.argv[1])





