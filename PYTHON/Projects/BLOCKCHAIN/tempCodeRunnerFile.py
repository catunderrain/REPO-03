def block(n):
    def cathash(data):
        data_in = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', ':', ';', ' ']
        data_out = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', ':', ';', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        datalist = list(data)
        print(data)
        datahashlist = []
        for j in range(len(datalist)):
            for i in range(len(data_in)):
                if datalist[j] == data_in[i]:
                    datahashlist.append(data_out[i])
        datahash = ''
        for i in range(len(datahashlist)):
            datahash += datahashlist[i]
        print(datahash)
        return datahash
    block = open(
        'c:\\noirecode\\python\\projects\\blockchain\\blocks\\block{}.txt'.format(n-1), 'r')
    blockread = block.read()
    keyhere = blockread.split('.')[1].split(',')[0]
    data = blockread.split(';')[0]
    passthere = cathash(data)

    print(keyhere)
    print(passthere)

    block.close()


block(1)
