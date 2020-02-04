import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import csv

import openfile

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]



color = ["#e41a1c", "#377eb8", "#4daf4a","#984ea3", "#ff7f00"]

t = open("wav_analysis/data/F0/long_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

for k in range(4):#人
    dataset = []
    for vowel in vowels:#母音
        d = []
        for key in range(4):#音高
            filename =  str(k+1)+ "/long/1_" +vowel+ "_" + str(key+1)
            fname = "wav_analysis/data/F0/" +filename+ ".txt"
    
            f0 = np.loadtxt(fname, delimiter=',')

            cent = 1200*np.log2(f0/pitch_Hz[key])

            
            d.append(np.mean(cent[200:1401]))

        dataset.append(d)

    np.savetxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', np.array(dataset), delimiter=',')