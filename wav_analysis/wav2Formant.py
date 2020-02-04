import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a']#,'i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]
updown = ['up', 'down']

for k in range(1):#2
    for j in range(1):#4
        for i in range(1):#2
            for vowel in vowels:
                for vowel_2 in vowels:
                    for key in range(1):  #3 
                        filename =  str(j+1)+ "/" +updown[k]+ "/" +str(i+1)+ "_" +vowel+ "_" +vowel_2+ "_" +keys[key]
                        fname = "recording/" +filename+ ".WAV"

                        try:
                            f = wave.open(fname, 'r')
                        except FileNotFoundError:
                            print(filename +' not exist!')
                            continue

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



                        N = 2048
                        windowed = np.hanning(N) * data[60000:60000+N]


                        fft_data = np.fft.fft(windowed)
                        freqList = np.fft.fftfreq(N, d=1.0/samplerate)

                        amp_data = np.abs(fft_data)

                        half = int(N/2)
                        fig = plt.figure()
                        plt.rcParams['font.family'] = 'Times'
                        ax = fig.add_subplot(312)
                        ax2 = fig.add_subplot(311)
                                                
                        ax.plot(freqList[0:half][0:half], amp_data[0:half])
                        ax.set_xlim(0, 2000)

                        ax2.plot(range(0,N), windowed)

                        ax3 = fig.add_subplot(313)
                        ax3.plot(freqList[0:half], np.log10(amp_data[0:half]))
                        ax3.set_xlim(0, 2000)
                        plt.show()
                        print(freqList[0:half])
