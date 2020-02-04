import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

import myFunc

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

time = np.linspace(0.,8.001,8001)

   
def graph_fix(ax):
    ax.hlines([0], 0, 8, "grey", linestyles='dashed')
    ax.vlines([1,7], -100, 100, "grey", linestyles='dashed')
    ax.set_xticks([0,2,4,6,8])
    ax.set_xlim(0,8)
    ax.set_ylim(-100,100)


for vowel in vowels:
    fig = plt.figure()

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
    



    #plt.legend()

    plt.show()