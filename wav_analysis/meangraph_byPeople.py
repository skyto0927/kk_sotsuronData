import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import csv

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

t = open("wav_analysis/data/F0/long_time.txt")
time_list = [float(data.strip()) for data in t.readlines()]
time = np.array(time_list)
t.close()

fig = plt.figure()

plt.rcParams['font.family'] = 'Times'
ax = fig.add_subplot(111)



marker = ["o", "^", "s", "x"]
color = ["#e41a1c", "#377eb8", "#4daf4a","#984ea3", "#ff7f00"]

alldata = []
for k in range(4):#人
    alldata.append(np.loadtxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', delimiter=','))
for x in range(5):
    for y in range(4):
        
        ax.plot(pitch_Hz, alldata[y][x], color=color[y], linewidth=1, linestyle="dashed", marker=marker[y], markersize=6, label=str(y+1))
        

    ax.hlines([0], pitch_Hz[0]*0.9, pitch_Hz[3]*1.1 , "grey", linestyles='dashed')
    ax.set_xscale('log')
    ax.set_xlim(pitch_Hz[0]*0.9,pitch_Hz[3]*1.1)
    ax.set_xticks([], minor=True)
    ax.set_xticks(pitch_Hz)
    ax.set_xticklabels(pitch)
    ax.set_ylabel('Variance')
    ax.set_xlabel('Pitch[Hz]')
    plt.tight_layout()
    plt.legend()

    #plt.show()
    plt.savefig("pitch_"+str(x+1)+".png")
    plt.cla()


alldata = []
for k in range(4):#人
    alldata.append(np.loadtxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', delimiter=',').T)
for x in range(4):
    for y in range(4):
        
        ax.plot(vowels, alldata[y][x], color=color[y], linewidth=1, linestyle="dashed", marker=marker[y], markersize=6, label=str(y+1))
        

    ax.hlines([0], 0, 4 , "grey", linestyles='dashed')
    ax.set_xticks([], minor=True)
    #ax.set_xticks(pitch_Hz)
    #ax.set_xticklabels(pitch)
    ax.set_ylabel('Variance')
    ax.set_xlabel('Vowels')
    plt.tight_layout()
    plt.legend()

    #plt.show()
    plt.savefig("vowels_"+str(x+1)+".png")
    plt.cla()



'''
for k in range(4):#人
    dataset = np.loadtxt('wav_analysis/data/statistics/var/'+str(k+1)+'_long.csv', delimiter=',')
    i = 0

    dataset_T = dataset.T
    for data in dataset_T:
        ax.plot(vowels, data, color=color[i], linewidth=1, linestyle="dashed", marker=marker[k], markersize=6, label=pitch[i])
        i+=1
    
    ax.hlines([0], 0, 4 , "grey", linestyles='dashed')
    ax.set_xticks([], minor=True)
    #ax.set_xticks(pitch_Hz)
    #ax.set_xticklabels(pitch)
    ax.set_ylabel('Variance')
    ax.set_xlabel('Vowels')
    plt.tight_layout()
    plt.legend()

    #plt.show()
    plt.savefig("vowels_"+str(k+1)+".png")
    plt.cla()
'''