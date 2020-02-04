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
for key in range(1):
    

    data = np.loadtxt("wav_analysis/data/ease/1/up.txt", delimiter=',')
    print(data)