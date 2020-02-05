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


for k in range(4):#人

    fig = plt.figure(figsize=(8,4))
    plt.rcParams['font.family'] = 'Times New Roman'

    
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    axs = [ax1,ax2,ax3,ax4,ax5]

    dataset = []
    for v in range(5):#母音
        for i in range(5):#母音
            for key in range(3):#音高
                filename = "1_"+vowels[v]+ "_"+ vowels[i]
                fname = "wav_analysis/data/F0/"+str(k+1)+ "/up/" +filename+ "_" + str(key+1)+ ".txt"
        
                f0 = np.loadtxt(fname, delimiter=',')

                #cent = 1200*np.log2(f0/pitch_Hz[key])

                
                axs[v].plot(time, f0, color=color[i] , linewidth=0.8)
                
    
            
        axs[v].set_yscale("log")

        axs[v].set_yticks([], minor=True)
        axs[v].set_yticks(pitch_Hz)
        axs[v].set_yticklabels(pitch)
        axs[v].set_ylim(pitch_Hz[0]*0.7,pitch_Hz[3]*1.3)
        axs[v].hlines(pitch_Hz, 0,2, "grey", linestyles='dashed')
        axs[v].vlines([1], 0,pitch_Hz[3]*1.1, "grey", linestyles='dashed')

        axs[v].set_title("Up: from /"+vowels[v]+"/")
                #plt.legend()
    plt.tight_layout()
    plt.savefig(str(k+1) + ".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.cla()


    #FFT 