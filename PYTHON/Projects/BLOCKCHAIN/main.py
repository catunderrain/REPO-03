import os
pathblock = 'c:\\noirecode\\python\\projects\\blockchain\\blocks\\block{}.txt'


def blockhash(n):
    # ma hoa du lieu
    print(' BLOCKHASH {}'.format(n))
    # ma hoa data

    def cathash(data):
        data_in = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', ':', ';', ' ', '!']
        data_out = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', '[', ']', '{', '}', ' ', '|', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        datalist = list(data)
        print('         Cathash.data:', data)
        datahashlist = []
        for j in range(len(datalist)):
            for i in range(len(data_in)):
                if datalist[j] == data_in[i]:
                    datahashlist.append(data_out[i])
        datahash = ''
        for i in range(len(datahashlist)):
            datahash += datahashlist[i]
        print('         Catahash.datahash:', datahash)
        return datahash

    # doc block
    block = open(pathblock.format(n), 'r')
    blockread = block.read()
    print('     BLOCKHASH.blockread:', blockread)

    # kiem tra massage trong hay day
    checkmessage = blockread.split(',')[1].split(':')[0]
    print('     BLOCKHASH.checkmessage:', checkmessage)
    if checkmessage == '':
        message = input('message: ')
        blockstart = blockread.split(',')[0]
        blockend = blockread.split(':')[1]
        block.close()
        block = open(pathblock.format(n), 'w')
        block.write(blockstart + ',' + message + ':' + blockend)
        block.close()
    else:
        block.close()

    # mo block de kiem tra pass
    block = open(pathblock.format(n), 'r')
    blockread = block.read()
    checkpass = blockread.split(';')[1]
    checkpassstart = blockread.split(';')[0]
    print('     BLOCKHASH.checkpass:', checkpass)
    # doc du lieu va ma hoa du lieu bang cathash
    data = blockread.split(';')[0]
    passthere = cathash(data)
    print('     BLOCKHASH.passthere:', passthere)
    # kiem tra lai pass co trung khop voi data khong
    if checkpass != '!' + passthere:
        block.close()
        block = open(pathblock.format(n), 'w')
        block.write(checkpassstart + ';!' + passthere)
        block.close()
    else:
        block.close()

    block = open(pathblock.format(n), 'r')
    print('     BLOCKHASH.dataafter:', block.read())
    block.close()
    return passthere


def newblock(n):
    print('NEWBLOCK {}'.format(n))
    block = open(
        pathblock.format(n), 'a')
    block.close()
    block = open(
        pathblock.format(n), 'r')
    blockread = block.read()
    if blockread == '':
        block.close()
        block = open(pathblock.format(n), 'w')
        block.write('keyhere{}.{},:passthere{};!'.format(
            n, blockhash(n-1), n+1))
        block.close()
        blockhash(n)
    else:
        block.close()
        blockhash(n)


def renderblock(n):
    for i in range(0, n+1):
        newblock(i)

# doc message tu block


def readblock(n):
    blocka = open(pathblock.format(n), 'r')
    blockaread = blocka.read()
    blockb = open(pathblock.format(n-1), 'r')
    blockbread = blockb.read()
    keya = blockaread.split('.')[1].split(',')[0]
    passb = blockbread.split('!')[1]
    if keya == passb:
        print('Message block {}: '.format(n),
              blockaread.split(',')[1].split(':')[0])
    else:
        print('BLOCK {}: DAMAGED BLOCKCHAIN!!! (BLOCK {})'.format(n, n-1))


# delete block
def delblock(n):
    for i in range(1, n+1):
        try:
            os.remove(pathblock.format(i))
            print('Remove block {}'.format(i))
        except:
            print('None {}'.format(i))


def encodeblock(n):
    block = open(pathblock.format(n), 'r')
    blockread = block.read()
    blockreadlist = list(blockread)
    print(blockreadlist)
    listnumber = ''
    for i in range(len(blockreadlist)):
        blockreadlist[i] = str(ord(blockreadlist[i]))
        listnumber += blockreadlist[i] + '.'
    listnumber = listnumber.rstrip('.')
    print(listnumber)


def decodeblock():
    strbl = '107.101.121.104.101.114.101.48.46.48.44.58.112.97.115.115.116.104.101.114.101.59.33'
    listbl = strbl.split('.')
    print(strbl)
    for i in range(len(listbl)):
        listbl[i] = chr(listbl[i])
        print(listbl[i])


for i in range(1, 21):
    readblock(i)
