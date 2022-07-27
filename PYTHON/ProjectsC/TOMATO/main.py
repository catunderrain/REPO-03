from datetime import datetime
from time import *
import winsound
from xml.etree.ElementTree import TreeBuilder

from tomlkit import date


def larm(x, n):
    mi = datetime.now().minute
    mip = mi + x
    if mip >= 60:
        mip -= 60
    mun = True
    while mun == True:
        minow = datetime.now().minute
        if mip != minow:
            print(n, datetime.now().strftime('%H:%M:%S'), mip)
            sleep(1)
        else:
            mun = False
    winsound.PlaySound("al.wav", winsound.SND_ALIAS)


def main():
    larm(20, 'Study 1 20m')
    larm(5, 'Break 1 5m')
    larm(20, 'Study 2 20m')
    larm(5, 'Break 2 5m')
    larm(20, 'Study 3 20m')
    larm(5, 'Break 3 20m')
    larm(20, 'Study 4 20m')
    larm(30, 'Break hard 30m')


while True:
    main()
