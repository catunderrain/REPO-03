import os
pathblock = 'c:\\noirecode\\python\\projects\\BLOCKCHAIN_V2\\blocks\\block{}.txt'


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
    decodeblock(n)
    block = open(pathblock.format(n), 'r')
    blockread = block.read()
    print('     BLOCKHASH.blockread:', blockread)

    # kiem tra massage trong hay day
    checkmessage = blockread.split(',')[1].split(':')[0]
    # print('     BLOCKHASH.checkmessage:', checkmessage)
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
    # print('     BLOCKHASH.checkpass:', checkpass)
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
    encodeblock(n)
    return passthere


def newblock(n):
    print('NEWBLOCK {}'.format(n))
    block = open(pathblock.format(n), 'a')
    block.close()
    block = open(pathblock.format(n), 'r')
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

# this is a def


def renderblock(n):
    for i in range(0, n+1):
        newblock(i)


def readblock(n):
    decodeblock(n)
    blocka = open(pathblock.format(n), 'r')
    blockaread = blocka.read()
    decodeblock(n-1)
    blockb = open(pathblock.format(n-1), 'r')
    blockbread = blockb.read()
    keya = blockaread.split('.')[1].split(',')[0]
    passb = blockbread.split('!')[1]
    if keya == passb:
        print('Message block {}: '.format(n),
              blockaread.split(',')[1].split(':')[0])
        encodeblock(n)
        encodeblock(n-1)
    else:
        print('BLOCK {}: DAMAGED BLOCKCHAIN!!! (BLOCK {})'.format(n, n-1))
        encodeblock(n)
        encodeblock(n-1)


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
    # print(blockread[:13])
    if blockread[:13] == 'catunderrain!':
        block.close()
    else:
        blockreadlist = list(blockread)
        # print(blockreadlist)
        listnumber = ''
        for i in range(len(blockreadlist)):
            blockreadlist[i] = str(ord(blockreadlist[i]))
            listnumber += blockreadlist[i] + '.'
        listnumber = listnumber.rstrip('.')
        # print(listnumber)
        block.close()
        block = open(pathblock.format(n), 'w')
        block.write('catunderrain!' + listnumber)
        block.close()


def decodeblock(n):
    block = open(pathblock.format(n), 'r')
    blockread = block.read()
    if blockread[:13] == 'catunderrain!':
        strbl = blockread[13:]
        listbl = strbl.split('.')
        # print(strbl)
        # print(listbl)
        strlist = ''
        for i in range(len(listbl)):
            strlist += chr(int(listbl[i]))
        # print(strlist)
        block.close()
        block = open(pathblock.format(n), 'w')
        block.write(strlist)
        block.close()
    else:
        block.close()
        print('Decode block {} failed'.format(n))


def countblock():
    count = 0
    i = 0
    while count == 0:
        try:
            block = open(pathblock.format(i), 'r')
            block.close()
            i += 1
        except:
            count = 1
    print('There are {} blocks now (include block 0)'.format(i))


def layout():
    exitquest = 'n'
    while exitquest == 'n':
        print('BLOCK CHAIN OF CAT')
        print('1. Render n block/render block n')
        print('2. Delete n block')
        print('3. Take message from block n')
        print('4. Exit')
        print('5. See how many block now')
        print('6. Clear screen')
        strin = input('Your chosen: ')
        if strin == '1':
            n = int(input('N: '))
            print('\n')
            renderblock(n)
            print('\n')
        elif strin == '2':
            n = int(input('N: '))
            print('\n')
            delblock(n)
            print('\n')
        elif strin == '3':
            n = int(input('N: '))
            print('\n')
            readblock(n)
            print('\n')
        elif strin == '5':
            print('\n')
            countblock()
            print('\n')
        elif strin == '6':
            print('\x1b[2J\x1b[1;1H')
        elif strin == '4':
            # nothing here this is just a comment
            exitquest = input('Exit y/n?:')
            if exitquest != 'y':
                exitquest = 'n'
# nothing here this is just a comment


layout()
