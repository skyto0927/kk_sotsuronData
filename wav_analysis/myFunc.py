import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import csv

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

def makeFilename(*args):
    name = '_'.join(map(str, args))
    return name

# long...f0s[people][vowel][pitch]
# updown...f0s[people][vowel1][vowel2][pitch]
def loadF0Files(type):
    f0s = []

    if type == "long":
        for i in range(4):#人
            f0 = []
            for j in range(5):#long a
                v = []
                for k in range(4): #Hz
                    fname = "wav_analysis/data/F0_1ms/"+str(i+1)+"/long/1_"+vowels[j]+"_"+str(k+1)+".txt"
                    v.append(np.loadtxt(fname, delimiter=','))
                f0.append(v)
            f0s.append(f0)

    elif type=="up" or type=="down":
        for i in range(4):#人
            f0 = []
            for j in range(5):
                v1 = []
                for j2 in range(5):
                    v2 = []
                    for k in range(3): #Hz
                        fname = "wav_analysis/data/F0/"+str(i+1)+"/"+type+"/1_"+vowels[j]+"_"+vowels[j2]+"_"+str(k+1)+".txt"
                        data = np.loadtxt(fname, delimiter=',')
                        v2.append(np.where(data>100, data, None))
                    v1.append(v2)
                f0.append(v1)
            f0s.append(f0)
    print("load complete.") 
    return f0s

#def updown_axis():

#def long_axis():
                

if __name__ == '__main__':

    a=loadF0Files("long")
    print(a)