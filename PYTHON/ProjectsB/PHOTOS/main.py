# import thu vien
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy
import csv
import random


# bung het array
numpy.set_printoptions(threshold=numpy.inf)

# set thong tin co ban
imgdata = image.imread('C:\\noirecode\\{}'.format('VA.jpg'))
print('Base shape: ', imgdata.shape)


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
def export(x, name):
    if name == '':
        n = 'result'
    else:
        n = name
    plt.imsave('{}.png'.format(n), x)


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


# gop 3 anh chuyen dung cho pool
def collapse2(x, y, z, t):
    line = []
    for i in range(len(x)):
        tup = []
        tup.append(x[i])
        tup.append(y[i])
        tup.append(z[i])
        line.append(tup)
    arr = []
    for j in range(int(t.shape[0])):
        row = []
        k = j*int(t.shape[1]/2)
        for i in range(int(t.shape[1]/2)):
            row.append(line[i + k])
        arr.append(row)
    arr = numpy.array(arr)
    return arr


# random image tra ve mang lon
def randimg():
    a = layer(imgdata, 1)
    b = layer(imgdata, 2)
    c = layer(imgdata, 3)
    for i in range(len(a)):
        a[i] = numpy.uint8(random.randint(0, 255))
        b[i] = numpy.uint8(random.randint(0, 255))
        c[i] = numpy.uint8(random.randint(0, 255))
    x = collapse(a, b, c)
    return x


# xuat anh RBG cua imgae
def rgbout(img, x):
    a = layer(img, 1)
    b = layer(img, 2)
    c = layer(img, 3)
    h = 255
    if x == 1:
        for i in range(len(a)):
            b[i] = numpy.uint8(h)
            c[i] = numpy.uint8(h)
        aa = collapse(a, b, c)
        export(aa, 'red')
    elif x == 2:
        for i in range(len(b)):
            a[i] = numpy.uint8(h)
            c[i] = numpy.uint8(h)
        bb = collapse(a, b, c)
        export(bb, 'green')
    elif x == 3:
        for i in range(len(c)):
            a[i] = numpy.uint8(h)
            b[i] = numpy.uint8(h)
        cc = collapse(a, b, c)
        export(cc, 'blue')
    else:
        print('None RGB')


# xuat anh goc ra ngoai
def default():
    a = layer(imgdata, 1)
    b = layer(imgdata, 2)
    c = layer(imgdata, 3)
    m = collapse(a, b, c)
    export(m)


# hien thi mau RGB
def showcolor(a, b, c):
    x = layer(imgdata, 1)
    y = layer(imgdata, 2)
    z = layer(imgdata, 3)
    a = numpy.uint8(a)
    b = numpy.uint8(b)
    c = numpy.uint8(c)
    for i in range(len(x)):
        x[i] = a
        y[i] = b
        z[i] = c
    m = collapse(x, y, z)
    export(m)


# pool 4x
def pool(img):
    a = layer(img, 1)
    b = layer(img, 2)
    c = layer(img, 3)
    x = []
    y = []
    z = []
    av = int(len(a)/2)
    for i in range(av):
        k = i*2
        max = numpy.uint8(0)
        for j in range(2):
            if a[j + k] > max:
                max = a[j + k]
        x.append(max)
    for i in range(av):
        k = i*2
        max = 0
        for j in range(2):
            if b[j + k] > max:
                max = b[j + k]
        y.append(max)
    for i in range(av):
        k = i*2
        max = 0
        for j in range(2):
            if c[j + k] > max:
                max = c[j + k]
        z.append(max)
    m = collapse2(x, y, z, img)
    for j in range(int(img.shape[0]/2)):
        k = j*2
        for t in range(int(img.shape[1]/2)):
            for i in range(3):
                if m[k][t][i] > m[k + 1][t][i]:
                    m[k + 1][t][i] = m[k][t][i]
                else:
                    m[k][t][i] = m[k + 1][t][i]
    h = []
    c = 0
    for row in m:
        if c == 0:
            h.append(row)
            c = 1
        else:
            c = 0
    h = numpy.array(h)
    h = cut(h)
    print(len(a))
    return h


# resize anh
def cut(x):
    s = list(x.shape)
    n = 2
    while s[0] % n != 0:
        s[0] -= 1
    while s[1] % n != 0:
        s[1] -= 1
    o = x[0:s[0], 0:s[1]]
    print('Shape cut: ', o.shape)
    return o


def randnoir(x):
    a = layer(x, 1)
    for i in range(len(a)):
        a[i] = numpy.uint8(random.randint(0, 255))
    b = a
    c = a
    h = collapse(a, b, c)
    export(h)


# workspace
