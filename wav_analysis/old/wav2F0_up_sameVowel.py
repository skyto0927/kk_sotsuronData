import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a']#,'i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]
i = 0
for vowel in vowels:
    fig = plt.figure()
    for key in range(3):
        fname = "recording/KaitoKobayashi/up/output" + str(i+int(key)) + ".WAV"

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


        '''
        _f0, _time = pw.dio(data, samplerate)
        f0 = pw.stonemask(data, _f0, _time, samplerate)
        '''

        f0, time = pw.harvest(data, samplerate)
        plt.plot(f0, label = pitch[key+1])

    plt.hlines(pitch_Hz, 0, 500, "grey", linestyles='dashed')
    plt.title('LongTone:'+vowel)
    plt.ylabel('Frequency[Hz]')
    plt.yscale("log")
    plt.yticks([174.6, 220, 261.6, 349.2], ['F3','A3','C4','F4'])
    plt.xlim(0,500)
    plt.ylim(150,375)
    #plt.legend()

    #fig.savefig("up_" +vowel+'.png', bbox_inches="tight", pad_inches=0.05)

    plt.show()
    i += 3