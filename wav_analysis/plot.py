import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

fig = plt.figure()
ax1 = fig.add_subplot(111)
for key in range(4):
    

    data = np.loadtxt("wav_analysis/data/statistics/var/"+str(key+1)+"_long.csv", delimiter=',')
    for d in data:
        ax1.plot(d)

ax1.set_ylabel('Variance')

plt.tight_layout()

    #plt.legend()

    #fig.savefig(vowel+'.png', bbox_inches="tight", pad_inches=0.05)

plt.show()