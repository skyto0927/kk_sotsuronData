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

fig = plt.figure()

plt.rcParams['font.family'] = 'Times'
ax = fig.add_subplot(111)



marker = ["$A$", "$I$", "$U$", "$E$", "$O$"]
colors = ["#e41a1c", "#377eb8", "#4daf4a","#984ea3", "#ff7f00"]

color = ['#550000', '#800000', '#aa0000', '#d50000', '#ff0000']

#横軸がピッチ

dataset = []
ease = []
for k in range(4):
    d = np.loadtxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', delimiter=',')
    e = np.loadtxt('wav_analysis/data/ease/'+str(k+1)+'/long.txt', delimiter=',')
    dataset.append(d)
    ease.append(e.astype(np.int16))

for k in range(4):#人
    for i in range(5):
        for j in range(4):
            if i == 0:
                ax.plot(ease[k][i][j], dataset[k][i][j], color=colors[j], linewidth=1, linestyle="dashed", marker=marker[i], markersize=6, label=pitch[j])
            else:
                ax.plot(ease[k][i][j], dataset[k][i][j], color=colors[j], linewidth=1, linestyle="dashed", marker=marker[i], markersize=6)
        #ax.errorbar(pitch_Hz, dataset[i], yerr=error[i], elinewidth=1, color=color[i], linewidth=1, linestyle="dashed", marker=marker[k], markersize=6, label=vowels[i], capsize=4)
    
    ax.hlines([0], -2, 6 , "grey", linestyles='dashed')
    #ax.set_xscale('log')
    ax.set_xlim(-0.5,4.5)
    ax.set_xticks([], minor=False)
    ax.set_xticks([0,1,2,3,4])
    ax.set_xticklabels([0,1,2,3,4])
    ax.set_ylabel('Cent_mean(cent)')
    ax.set_xlabel('Difficulty')
    plt.tight_layout()
    plt.legend()
    ax.set_ylim(-60,60)

    #plt.show()
    plt.savefig("ease_"+str(k+1)+".png")
    #plt.savefig("pitch.png")
    plt.cla()



#横軸が母音

'''
for k in range(4):#人
    e = np.loadtxt('wav_analysis/data/ease/'+str(k+1)+'/long.txt', delimiter=',').T
    ease = e.astype(np.int16)
    dataset = np.loadtxt('wav_analysis/data/statistics/mean/'+str(k+1)+'_long.csv', delimiter=',').T
    error = np.sqrt(np.loadtxt('wav_analysis/data/statistics/var/'+str(k+1)+'_long.csv', delimiter=',')).T

    for i in range(4):
        for j in range(5):
            ax.plot(vowels[j], dataset[i][j], color=color[ease[i][j]], linewidth=1, linestyle="dashed", marker=marker[i], markersize=6, label=pitch[i])
        #ax.errorbar([0,1,2,3,4], dataset[i], yerr=error[i], elinewidth=1, color=color[i], linewidth=1, linestyle="dashed", marker=marker[k], markersize=6, label=pitch[i], capsize=4)
    
    ax.hlines([0], 0,4, "grey", linestyles='dashed')
    ax.set_xticks([], minor=True)
    ax.set_xticks([0,1,2,3,4])
    ax.set_xticklabels(vowels)
    ax.set_ylabel('Cent_mean(cent)')
    ax.set_xlabel('Vowel')
    plt.tight_layout()
    #plt.legend()

    #plt.show()
    #plt.savefig("vowel.png")

    plt.savefig("vowel_"+str(k+1)+".png")

    plt.cla()


'''