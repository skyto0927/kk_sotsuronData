import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]
'''
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
'''
for key in range(5):
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    fname = "recording/KaitoKobayashi/down/a/" + str(int(key)+1) + ".WAV"

    f = wave.open(fname, 'r')

    ch = f.getnchannels()
    samplewidth = f.getsampwidth()
    samplerate = f.getframerate()
    samplesize = f.getnframes()

    buf = f.readframes(samplesize)
    f.close()

    #ndarrayに変換
    data = np.frombuffer(buf, dtype='int16')
    data = data/32768.0#正規化している

    #ステレオなので左のみ取り出す
    if ch == 2:
        data = data[0::2]


    f0, time = pw.harvest(data, samplerate)
    cent = [0]*len(f0)
    for k in range(len(f0)):
        if f0[k] == 0:
            cent[k] = 0
        elif time[k] < 1:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[1])
        elif 1 <= time[k] < 2:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[0])
        elif 4< time[k] < 5:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[2])
        elif 5 <= time[k] < 6:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[0])
        elif 8< time[k] < 9:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[3])
        elif 9 <= time[k] < 10:
            cent[k] = 1200*np.log2(f0[k]/pitch_Hz[0])
        else:
            cent[k] = 0



    ax1.plot(time, f0, label = vowels[key])
    ax2.plot(time, cent)
    ax3.plot(data)


    ax1.hlines(pitch_Hz, 0, 12, "grey", linestyles='dashed')
    ax1.vlines([1,2,4,5,6,8,9,10], 0, 500, "grey", linestyles='dashed')
    ax1.set_title('Down: a to '+vowels[key])
    ax1.set_ylabel('Frequency[Hz]')
    ax1.set_yscale("log")
    ax1.set_yticks([], minor=True)
    ax1.set_yticks(pitch_Hz)
    ax1.set_yticklabels(pitch)
    ax1.set_xlim(0,12)
    ax1.set_ylim(150,375)

    ax2.hlines([0], 0, 12, "grey", linestyles='dashed')
    ax2.vlines([1,2,4,5,6,8,9,10], -100, 100, "grey", linestyles='dashed')
    ax2.set_xticks([0,2,4,6,8,10])
    ax2.set_ylabel('Cent')
    ax2.set_xlim(0,12)
    ax2.set_ylim(-100,100)

    ax3.set_xticks([0,44100*2, 44100*4, 44100*6, 44100*8, 44100*10])
    ax3.set_xticklabels([0,2,4,6,8,10])

    ax3.set_xlim(0,44100*12)
    plt.tight_layout()
    #plt.legend()

    fig.savefig("down_a_" +vowels[key]+'.png', bbox_inches="tight", pad_inches=0.05)

    #plt.show()