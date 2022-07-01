from numpy import sin, pi, linspace, concatenate, max, int16, append
import os
from scipy.io.wavfile import write
import random
samplerate = 44100


def waveform(freq, duration=0.2):
    amplitude = 4096
    t = linspace(0, duration, int(samplerate*duration + 1))
    wave = amplitude*sin(2*pi*freq*t)
    return wave


def notelist():
    basefreq = 160
    notefreqs = [basefreq*pow(2, (i/12)) for i in range(0, 36)]
    # notefreqs['x'] = 0
    return notefreqs


try:
    os.remove('melody.wav')
except:
    print('Nothing to remove')


def typeA():

    def x():
        def notefunc(i, note):
            if i == 0:
                return [note, note + 4, note + 7, note + 11]*4
            if i == 1:
                return [note, note + 3, note + 7, note + 12]*4

        rannote = random.randint(0, 23)
        chord = notefunc(random.randint(0, 1), rannote)
        x = []
        for i in chord:
            x.append(notelist()[i])

        a = []
        for i in x:
            az = waveform(i)
            a.append(az)
        a = concatenate(a)
        return a

    a = []
    a.append(x())
    a.append(x())
    a.append(x())
    a.append(x())
    a = concatenate(a)
    a = a*(16300/max(a))
    y = a.astype(int16)
    write('melody.wav', 44100, y)


typeA()
