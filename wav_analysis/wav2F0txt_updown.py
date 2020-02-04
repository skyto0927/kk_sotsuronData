import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]
updown = ['up', 'down']

for k in range(2):#2
    for j in range(4):#4
        for i in range(2):#2
            for vowel in vowels:
                for vowel_2 in vowels:
                    for key in range(3):  #3 
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



                        #_f0, _time = pw.dio(data, samplerate)
                        #f0 = pw.stonemask(data, _f0, _time, samplerate)
                        f0, time = pw.harvest(data, samplerate)

                        #cent = 1200*np.log2(f0/pitch_Hz[key])
                        f0_str = [str(n) for n in f0]
                        #time_str = [str(n) for n in time]

                        str_ = '\n'.join(f0_str)
                        with open("wav_analysis/data/F0/" +filename+ ".txt", 'wt') as ff:
                            ff.write(str_)

                        '''
                        str_2 = '\n'.join(time_str)
                        with open("wav_analysis/data/F0/updown_time.txt", 'wt') as ff:
                            ff.write(str_2)
                        '''
                        

