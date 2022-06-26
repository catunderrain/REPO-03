import numpy as np
import random

samplerate = 4400

def wave(freq, duration = 0.20):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave


def pianonotes():
    octave = ['c',
              'C',
              'd',
              'D',
              'e',
              'f',
              'F',
              'g',
              'G',
              'a',
              'A',
              'b',
              'c1',
              'C1',
              'd1',
              'D1',
              'e1',
              'f1',
              'F1',
              'g1',
              'G1',
              'a1',
              'A1',
              'b1',
              'c2',
              'C2',
              'd2',
              'D2',
              'e2',
              'f2',
              'F2',
              'g2',
              'G2',
              'a2',
              'A2',
              'b2'
              ] 
    basefreq = 261.63
    notefreqs = {octave[i]: basefreq * pow(2,(i/12)) for i in range(len(octave))}        
    notefreqs['x'] = 0.0
    return notefreqs


def randnote(numnote, string, add):
    g = mang = [] 
    mang = np.array([string[i] for i in range(len(string))]).tolist() + add
    for i in range(numnote):
       x = random.randint(0, len(mang) - 1)
       g.append(mang[x]) 
    g = [g[i] + '-' for i in range(len(g))]
    final = ''.join(g)[:2*len(g) - 1]
    return final


def songdata(musicnotes):
    notefreqs = pianonotes()
    song = [wave(notefreqs[note]) for note in musicnotes.split('-')]
    song = np.concatenate(song)
    return song
