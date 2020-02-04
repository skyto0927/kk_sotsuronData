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

t = open("wav_analysis/data/F0/updown_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

color = ["#e41a1c", "#377eb8", "#4daf4a","#984ea3", "#ff7f00"]

fig = plt.figure()

ax = fig.add_subplot(111)

for k in range(4):#人
    dataset = []
    for vowel in vowels:#母音
        for i in range(5):#母音
            for key in range(3):#音高
                filename = "1_"+vowel+ "_"+ vowels[i]
                fname = "wav_analysis/data/F0/"+str(k+1)+ "/up/" +filename+ "_" + str(key+1)+ ".txt"
        
                f0 = np.loadtxt(fname, delimiter=',')

                cent = 1200*np.log2(f0/pitch_Hz[key])

                
                ax.plot(time, f0, color=color[i] , linewidth=1)
                
    
            plt.tight_layout()
            ax.set_yscale("log")

            ax.set_yticks([], minor=True)
            ax.set_yticks(pitch_Hz)
            ax.set_yticklabels(pitch)
            ax.set_ylim(pitch_Hz[0]*0.9,pitch_Hz[3]*1.1)
            ax.hlines(pitch_Hz, 0,2, "grey", linestyles='dashed')
            ax.vlines([1], 0,pitch_Hz[3]*1.1, "grey", linestyles='dashed')

            
                #plt.legend()

        plt.savefig(str(k+1) + "_"+vowel+".png")
        plt.cla()


    #FFT 