import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy
import csv
import random

# bung het array
numpy.set_printoptions(threshold=numpy.inf)

# set thong tin co ban
imgdata = image.imread('C:\\noirecode\\{}'.format('VA.jpg'))


# chuyen du lieu sang file csv
def writecsv(x):
    with open('matrix.csv', 'w') as matrix:
        # viet hang so dau tien
        for i in range(1, len(x) + 1):
            if i == len(x):
                matrix.write(str(i))
            else:
                matrix.write(str(i) + ',')
        matrix.write('\n\n')

        # them cac dong thong so
        writer = csv.writer(matrix)
        for i in range(len(x)):
            writer.writerow(x[i])

    return 'Write done'


# lam tron cac du lieu trong mang
def roundx(x, n):
    for row in x:
        for node in row:
            for i in range(3):
                node[i] = round(node[i], n)

    return x


# xuat anh da chuyen tu du lieu ra ngoai
def export(x):
    plt.imsave('result.png', x)


# tach anh thanh 3 layer RBG
def layer(x, key):
    l1 = []
    l2 = []
    l3 = []
    for row in x:
        for node in row:
            l1.append(node[0])
            l2.append(node[1])
            l3.append(node[2])
    if key == 1:
        return l1
    elif key == 2:
        return l2
    elif key == 3:
        return l3
    else:
        return 'None layer'


# gop 3 layer lai thanh mot array lon
def collapse(x, y, z):

    line = []
    for i in range(len(x)):
        tup = []
        tup.append(x[i])
        tup.append(y[i])
        tup.append(z[i])
        line.append(tup)

    arr = []
    for j in range(imgdata.shape[0]):
        row = []
        k = j*imgdata.shape[1]
        for i in range(imgdata.shape[1]):
            row.append(line[i + k])
        arr.append(row)

    arr = numpy.array(arr)

    return arr


# for i in range(len(a)):
#     d = 100
#     if a[i] < d and b[i] < d and c[i] < d:
#         a[i] = b[i] = c[i] = numpy.uint8(255)


# random image tra ve mang lon
def randimg():
    for i in range(len(a)):
        a[i] = numpy.uint8(random.randint(50, 60))
        b[i] = numpy.uint8(random.randint(50, 60))
        c[i] = numpy.uint8(random.randint(50, 60))

    x = collapse(a, b, c)
    export(x)


# workspace
a = layer(imgdata, 1)
b = layer(imgdata, 2)
c = layer(imgdata, 3)
m = collapse(a, b, c)
randimg()
