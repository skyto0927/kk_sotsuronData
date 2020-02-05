import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a']#,'i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

t = open("wav_analysis/data/F0/updown_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

for i in range(4)
    fig = plt.figure(figsize=(8,4))
    plt.rcParams['font.family'] = 'Times New Roman'

    
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    for vowel in vowels:
        for vowel_2 in vowels:
            for key in range(1):
                filename =  str(i+1)+"/up/1_"+vowel+"_"+vowel_2+"_"+str(key+1)
                fname = "wav_analysis/data/F0/" +filename+ ".txt"

                f = open(fname)
                f0_list = [float(data.strip()) for data in f.readlines()]
                f0 = np.array(f0_list)
                f.close()
                
                cent = 1200*np.log2(f0/pitch_Hz[key])

                ax1.plot(time, f0, label = pitch[key])
                ax2.plot(time, cent)

            
            ax1.hlines(pitch_Hz, 0, 8, "grey", linestyles='dashed')
            ax1.set_title('LongTone:'+vowel)

            ax1.set_xticks([0,2,4,6,8])
            ax1.set_ylabel('Frequency[Hz]')
            ax1.set_yscale("log")
            ax1.set_yticks([], minor=True)
            ax1.set_yticks(pitch_Hz)
            ax1.set_yticklabels(pitch)
            ax1.set_xlim(0,2)
            ax1.set_ylim(150,375)

            ax2.hlines([0,400], 0, 8, "grey", linestyles='dashed')
            ax2.vlines([1,7], -100, 500, "grey", linestyles='dashed')
            ax2.set_xticks([0,2,4,6,8])
            ax2.set_ylabel('Cent[cent]')
            ax2.set_xlim(0,2)
            ax2.set_ylim(-100,500)

            plt.tight_layout()

            #plt.legend()

            #fig.savefig(vowel+'.png', bbox_inches="tight", pad_inches=0.05)

            #plt.show()