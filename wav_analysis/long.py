import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import seaborn as sns
import pandas as pd

import myFunc

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

all_pitch = [164.8,185,196,207.6,233,246.9,277.1,293.6,311.1,329.6,369.9,391.9]

pitch_colors = sns.color_palette(n_colors=24)[0:4]
vowel_colors = sns.color_palette(n_colors=24)[5:10]

time = np.linspace(0.,8.001,8001)

   
def graph_fix(ax):
    ax.hlines([0], 0, 8, "grey", linestyles='dashed')
    ax.vlines([1,7], -100, 100, "grey", linestyles='dashed')
    ax.set_xticks([0,2,4,6,8])
    ax.set_xlim(0,8)
    ax.set_ylim(-100,100)

#dataset = myFunc.loadF0Files("long")

N=512
s = 16
framerate = 1000
for i in range(4):#人
    fig = plt.figure(figsize=(8,4))
    plt.rcParams['font.family'] = 'Times New Roman'

    
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)

    axs = [ax1,ax2,ax3,ax4,ax5]
    for j in range(5):#母音
        

        for k in range(4):#ピッチ
            fname = "wav_analysis/data/F0_1ms/"+str(i+1)+"/long/1_"+vowels[j]+"_"+str(k+1)+".txt"
            dataset = (np.loadtxt(fname, delimiter=','))
                
            

            time = np.linspace(0,8,8001)
            axs[j].plot(time,dataset, linewidth=0.8, color=pitch_colors[k])



        axs[j].hlines(all_pitch, -1, 9 , "grey", linestyles='dashed', linewidth=0.5)
        axs[j].hlines(pitch_Hz, -1, 9 , "grey", linestyles='dashed', linewidth=1)
        axs[j].set_yscale("log")
        axs[j].set_yticks(pitch_Hz)
        axs[j].set_yticks([],minor=True)
        axs[j].set_yticklabels(pitch)
        axs[j].set_ylim(pitch_Hz[0]*0.9, pitch_Hz[3]*1.1)
        axs[j].set_xticks([0,2,4,6,8])
        axs[j].set_xlim(0,8)
        
        axs[j].set_title("/"+vowels[j]+"/")

#fig.suptitle(str(i+1))

        #plt.show()
    plt.tight_layout()
    fig.savefig(str(i+1)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.cla()
'''         
            ax1 = fig.add_subplot(411)
            ax2 = fig.add_subplot(412)
            ax3 = fig.add_subplot(413)
            ax4 = fig.add_subplot(414)
            axs = [ax1, ax2, ax3, ax4]



    for key in range(4):
        filename =  "1/long/1_" +vowel+ "_" + str(key+1)
        fname = "wav_analysis/data/F0_1ms/" +filename+ ".txt"
        f0 = np.loadtxt(fname, delimiter=',')
        cent = 1200*np.log2(f0/pitch_Hz[key])

        axs[key].plot(time, cent)


        graph_fix(axs[key])
    

'''

    #plt.legend()

    