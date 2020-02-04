import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

t = open("wav_analysis/data/F0/long_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()
fig = plt.figure()


ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

axs = [ax1, ax2, ax3, ax4]
   
def graph_fix(ax):
    ax.hlines([0], 0, 8, "grey", linestyles='dashed')
    ax.vlines([1,7], -100, 100, "grey", linestyles='dashed')
    ax.set_xticks([0,2,4,6,8])
    ax.set_ylabel('Cent[cent]')
    ax.set_xlim(0,8)
    ax.set_ylim(-100,100)

for key in range(4):
    for vowel in vowels:
        filename =  "1/long/1_" +vowel+ "_" + str(key+1)
        fname = "wav_analysis/data/F0/" +filename+ ".txt"
        f0 = np.loadtxt(fname, delimiter=',')
        cent = 1200*np.log2(f0/pitch_Hz[key])

        axs[key].plot(time, cent)


    graph_fix(axs[key])
    

plt.tight_layout()

    #plt.legend()

plt.show()