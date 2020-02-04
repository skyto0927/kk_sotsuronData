import numpy as np
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a']#,'i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

for key in range(1):
    fig = plt.figure()
    for vowel in vowels:
        #fname = "recording/KaitoKobayashi/long/" + vowel + keys[key] + ".WAV"
        fname = "recording/KaitoKobayashi/単音.WAV"
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
        #data = data/32768.0#正規化している

        #ステレオなので左のみ取り出す
        if ch == 2:
            data = data[0::2]

        data_pow = np.power(data,2)
        N = 1024
        step = 512
        i = 0
        pow = []
        while samplesize > i+N:
            p = np.sum(data_pow[i:i+N])/N
            pow.append(p)
            i += step

        pow_log = 10*np.log10(pow)

        length = len(pow_log)
        t = 512/samplerate
        x = []
        for k in range(length):
            x.append(t*k)
        
        plt.subplot(211)
        plt.plot(data)

        plt.subplot(212)
        plt.plot(x, pow_log, label = vowel)
        

    #plt.title('LongTone:'+pitch[key])

    #plt.xlim(0,2000)
    #plt.ylim(150,375)

    #plt.legend()

    fig.savefig('pow.png', bbox_inches="tight", pad_inches=0.05)

    plt.show()