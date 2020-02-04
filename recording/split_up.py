import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import struct

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']

name = ["miyazawa", "gorai", "ozuru", "kobayashi"]

for j in range(4):
    for k in range(2):
                

        for key in range(5):
            try:
                fname = "recording/"+name[j]+ "_" +str(k+1) +"/up/" +vowels[key]+ ".WAV"
            except FileNotFoundError:
                    print("No such file!")
                    continue

            f = wave.open(fname, 'r')

            ch = f.getnchannels()
            samplewidth = f.getsampwidth()
            samplerate = f.getframerate()
            samplesize = f.getnframes()

            buf = f.readframes(samplesize)
            f.close()

            #ndarrayに変換
            data = np.frombuffer(buf, dtype='int16')

            #ステレオなので左のみ取り出す
            if ch == 2:
                data = data[0::2]

            for i in range(5):
                for l in range(3):
                    outf = "recording/0" +str(j+1)+ "/up/" +str(k+1)+ "_" +vowels[key]+ "_" +vowels[i]+ "_" +keys[l]+ ".WAV"
                

                    big_interval = 16*samplerate
                    interval = 4*samplerate
                    length = 2*samplerate

                    outd = struct.pack("h"*length, *data[i*big_interval +  l*interval : i*big_interval + length + l*interval])
                    ww = wave.open(outf, 'w')
                    ww.setnchannels(ch)
                    ww.setsampwidth(samplewidth)
                    ww.setframerate(samplerate)
                    ww.writeframes(outd)
                    ww.close()

    
#longは8秒→8秒休み
#up,downは2秒→2秒休み
#10秒1セット→6秒休み


