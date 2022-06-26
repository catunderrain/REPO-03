import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from MainSub import pianonotes, randnote, songdata
import os
import random
try:
    os.remove('main.wav')
except:
    print('none')
inputstring = 'e'

inputadd = []
inputnumber = 1
samplerate = 4400
notefreqs = pianonotes()
musicnotes = randnote(inputnumber, inputstring, inputadd)
data = songdata(musicnotes)
data = data * (16300/np.max(data))  # đưa data cao nhất lên 16300
y = data.astype(np.int16)

for i in range(0, 880):
    y[i] = random.randint(-16200, 16200)
write('main.wav', 4400, y)
print(musicnotes)
# x = [i for i in range(len(y))]
# plt.plot(x, y)
# plt.show()
obj = wave.open('a.wav', 'r')
print(obj)
obj.close()
