import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import csv

import myFunc

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

t = open("wav_analysis/data/F0/long_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

color = ["#e41a1c", "#377eb8", "#4daf4a","#984ea3", "#ff7f00"]

fig = plt.figure()

plt.rcParams['font.family'] = 'Times'
ax = fig.add_subplot(111)


f0s = myFunc.loadF0Files("long")

N = 4#Nは1,2,3,4,5,6,8,10

'''
for i in range(4):#人
    for k in range(4):#音高
        for j in range(5):#母音
        
            
            cent = 1200*np.log2(f0s[i][j][k]/pitch_Hz[k])
            d = []
            error = []

            
            dn = int(1200/N)
            for n in range(N):
                d.append(np.mean(cent[(200+n*dn):int(201+(n+1)*dn)]))

            
                error.append(np.std(cent[(200+n*dn):int(201+(n+1)*dn)]))
            
            #ax.plot([1,2], d, color=color[i] , linewidth=1)
            x = np.array(range(1,N+1),dtype='int64')
            a,b = np.polyfit(x, d, 1)

            y = a*x + b
            ax.plot(x, y, color=color[j] , linewidth=1, linestyle="dashed")

            ax.errorbar(range(1,N+1), d, yerr=error, elinewidth=1, color=color[j], linewidth=0, linestyle="dashed", marker="o", markersize=6, capsize=4, label=vowels[j])
    

        #plt.tight_layout()
        #ax.set_yscale("log")
        #ax.set_yticks(pitch_Hz)
        #ax.set_yticklabels(pitch)
        ax.set_xlim(0.9, N+0.1)
        ax.set_xticks(range(1,N+1), minor=False)
        ax.set_xticklabels(range(1,N+1))
        ax.set_ylim(-80,80)
        ax.hlines(0, 0,N+1, "grey", linestyles='dashed')
        ax.set_ylabel("Cent[cent]")

        plt.legend()
        plt.savefig(str(i+1)+"_"+pitch[k]+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
        plt.cla()
'''
    #ax.vlines([1], 0, pitch_Hz[3]*1.1, "grey", linestyles='dashed')

    #np.savetxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', np.array(dataset), delimiter=',')


for i in range(4):#人
    for j in range(5):#母音
        for k in range(4):#音高
        
            
            cent = 1200*np.log2(f0s[i][j][k]/pitch_Hz[k])
            d = []
            error = []

            
            dn = int(1200/N)
            for n in range(N):
                d.append(np.mean(cent[(200+n*dn):int(201+(n+1)*dn)]))

            
                error.append(np.std(cent[(200+n*dn):int(201+(n+1)*dn)]))
            
            #ax.plot([1,2], d, color=color[i] , linewidth=1)
            x = np.array(range(1,N+1),dtype='int64')
            a,b = np.polyfit(x, d, 1)

            y = a*x + b
            ax.plot(x, y, color=color[k] , linewidth=1, linestyle="dashed")

            ax.errorbar(range(1,N+1), d, yerr=error, elinewidth=1, color=color[k], linewidth=0, linestyle="dashed", marker="o", markersize=6, capsize=4, label=pitch[k])
    

        #plt.tight_layout()
        #ax.set_yscale("log")
        #ax.set_yticks(pitch_Hz)
        #ax.set_yticklabels(pitch)
        ax.set_xlim(0.9, N+0.1)
        ax.set_xticks(range(1,N+1), minor=False)
        ax.set_xticklabels(range(1,N+1))
        ax.set_ylim(-80,80)
        ax.hlines(0, 0,N+1, "grey", linestyles='dashed')
        ax.set_ylabel("Cent[cent]")

        plt.legend()
        plt.savefig(str(i+1)+"_"+vowels[j]+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
        plt.cla()