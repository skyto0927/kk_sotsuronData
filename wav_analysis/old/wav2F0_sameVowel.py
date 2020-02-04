import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a']#,'i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

for vowel in vowels:
    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    for key in range(1):
        fname = "recording/01/long/1_" +vowel+ "_" +keys[key]+ ".WAV"

        f = wave.open(fname, 'r')

        ch = f.getnchannels()
        samplewidth = f.getsampwidth()
        samplerate = f.getframerate()
        samplesize = f.getnframes()

        '''
        print("チャンネル数:", ch)
        print("サンプル幅:", samplewidth)
        print("レート:", samplerate)
        print("サンプル数:", samplesize)
        '''

        buf = f.readframes(samplesize)
        f.close()

        #ndarrayに変換
        data = np.frombuffer(buf, dtype='int16')
        data = data/32768.0#正規化している

        #ステレオなので左のみ取り出す
        if ch == 2:
            data = data[0::2]



        #_f0, _time = pw.dio(data, samplerate)
        #f0 = pw.stonemask(data, _f0, _time, samplerate)
        f0, time = pw.harvest(data, samplerate)

        cent = 1200*np.log2(f0/pitch_Hz[key])

        ax1.plot(time, f0, label = pitch[key])
        ax2.plot(time, cent)
        ax3.plot(data)

    
    ax1.hlines(pitch_Hz, 0, 9, "grey", linestyles='dashed')
    ax1.set_title('LongTone:'+vowel)

    ax1.set_xticks([0,2,4,6,8])
    ax1.set_ylabel('Frequency[Hz]')
    ax1.set_yscale("log")
    ax1.set_yticks([], minor=True)
    ax1.set_yticks(pitch_Hz)
    ax1.set_yticklabels(pitch)
    ax1.set_xlim(0,9)
    ax1.set_ylim(150,375)

    ax2.hlines([0], 0, 9, "grey", linestyles='dashed')
    ax2.set_xticks([0,2,4,6,8])
    ax2.set_ylabel('Frequency[Hz]')
    ax2.set_xlim(0,9)
    ax2.set_ylim(-100,100)

    ax3.set_xticks([0,44100*2, 44100*4, 44100*6, 44100*8, 44100*10])
    ax3.set_xticklabels([0,2,4,6,8,10])
    
    ax3.set_xlim(0,44100*9)
    plt.tight_layout()

    #plt.legend()

    #fig.savefig(vowel+'.png', bbox_inches="tight", pad_inches=0.05)

    plt.show()