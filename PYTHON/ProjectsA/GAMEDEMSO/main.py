import random
import time


def fast(x):
    print('\x1b[2J\x1b[1;1H')
    a = random.randint(0, x)
    b = random.randint(0, x)
    check = 0
    i = time.perf_counter()
    while check == 0:
        print(a, '+', b, '=')
        ans = int(input())
        if ans == a+b:
            print('True')
            j = time.perf_counter()
            print(round(j - i, 3))
            check = 1
            return j - i

        else:
            print('Wrong')


def fastfather(n, x):
    table = []
    for i in range(n):
        print('NUMBER {}'.format(i+1))
        table.append(fast(x))
    print('\x1b[2J\x1b[1;1H')
    print('Time table')
    for i in range(n):
        print(round(table[i], 3))
    print('Max:', round(max(table), 3))
    print('Min:', round(min(table), 3))


def layout():
    exitquest = 'n'
    while exitquest == 'n':
        n = int(input('Nhap so luong thuat toan: '))
        x = int(input('Nhap gioi han phan tu: '))
        fastfather(n, x)
        exitquest = input('Exit y/n?: ')
        if exitquest != 'y':
            exitquest = 'n'


layout()
