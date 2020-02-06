import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import csv
import seaborn as sns
import pandas as pd

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

t = open("wav_analysis/data/F0/updown_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

vowel_colors = sns.color_palette(n_colors=24)[5:10]
color = sns.husl_palette(3)

for k in range(4):#人

    fig = plt.figure()
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams["font.size"] = 8

    
    

    dataset = []
    for v in range(5):#母音
        for i in range(5):#母音
            ax = fig.add_subplot(5,5,v*5+i+1)
            for key in range(3):#音高
                filename = "1_"+vowels[v]+ "_"+ vowels[i]
                fname = "wav_analysis/data/F0/"+str(k+1)+ "/up/" +filename+ "_" + str(key+1)+ ".txt"
        
                f0 = np.loadtxt(fname, delimiter=',')

                #cent = 1200*np.log2(f0/pitch_Hz[key])

                
                ax.plot(time, f0, color=color[key] , linewidth=1)
                
    
            
            ax.set_yscale("log")
            ax.set_xlim(0,2)

            ax.set_yticks([], minor=True)
            ax.set_yticks(pitch_Hz)
            ax.set_yticklabels(pitch)
            ax.set_ylim(pitch_Hz[0]*0.8,pitch_Hz[3]*1.2)
            ax.hlines(pitch_Hz, 0,2, "grey", linestyles='dashed',linewidth=1)
            ax.vlines([1], 0,pitch_Hz[3]*1.2, "grey", linestyles='dashed',linewidth=1)
            if v*5+i != 20:
                ax.set_yticks([])
                ax.set_xticks([])

            #ax.set_xlabel("Time[Hz]")
            #ax.set_ylabel("Pitch")
                    #plt.legend()
    plt.tight_layout()
    plt.savefig("F0_up_"+str(k+1)+".eps", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.cla()


    #FFT  