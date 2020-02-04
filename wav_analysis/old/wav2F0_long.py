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

for key in range(4):
    for vowel in vowels:
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



        _f0, _time = pw.dio(data, samplerate)
        f0 = pw.stonemask(data, _f0, _time, samplerate)

        plt.plot(f0, label = vowel)

    plt.title('LongTone:'+pitch[key])
    plt.ylim(pitch_Hz[key]-25, pitch_Hz[key]+25)
    plt.ylabel('Frequency[Hz]')
    plt.legend()

    fig.savefig(pitch[key]+'.png', bbox_inches="tight", pad_inches=0.05)

    plt.show()