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

t = open("wav_analysis/data/F0/long_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()


for k in range(4):
    dataset = []
    for vowel in vowels:
        for vowel_2 in vowels:
            for key in range(3):
                filename =  "1/long/1_" +vowel+ "_" +vowel_2+ "_" + str(key+1)
                fname = "wav_analysis/data/F0/" +filename+ ".txt"

                f = open(fname)
                f0_list = [float(data.strip()) for data in f.readlines()]
                f0 = np.array(f0_list)
                f.close()

                cent = 1200*np.log2(f0/pitch_Hz[0])

                d = []
                d.append(np.mean(cent[100:301]))
                d.append(np.var(cent[100:301]))
                d.append(np.max(cent[100:301]))
                d.append(np.min(cent[100:301]))

                dataset.append(d)

    np.savetxt('wav_analysis/data/statistics/'+str(k+1)+'_long.csv', np.array(dataset), delimiter=',')