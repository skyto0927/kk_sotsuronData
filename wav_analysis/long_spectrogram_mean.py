import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import pyworld as pw
import seaborn as sns
import pandas as pd

import myFunc

vowels = ['a','i','u','e','o']
keys = ['1','2','3','4']
pitch = ['F3','A3','C4','F4']
pitch_Hz = [174.6, 220, 261.6, 349.2]

time = np.linspace(0.,8.001,8001)

   
def graph_fix(ax):
    ax.hlines([0], 0, 8, "grey", linestyles='dashed')
    ax.vlines([1,7], -100, 100, "grey", linestyles='dashed')
    ax.set_xticks([0,2,4,6,8])
    ax.set_xlim(0,8)
    ax.set_ylim(-100,100)

#dataset = myFunc.loadF0Files("long")

N=500
s = 50
framerate = 1000

window = np.hamming(N)
for i in range(4):#人
    fig = plt.figure()
    plt.rcParams['font.family'] = 'Times New Roman'
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)

    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)

    axs1 = [ax1,ax2,ax3,ax4,ax5]

    for j in range(5):#母音
        for k in range(4):#ピッチ
        
            fname = "wav_analysis/data/F0_1ms/"+str(i+1)+"/long/1_"+vowels[j]+"_"+str(k+1)+".txt"
            dataset = (np.loadtxt(fname, delimiter=','))[1000:7001]

            cent = 1200*np.log2(dataset/pitch_Hz[k])
            
            ampList = []
            max = int(N/2)

            freq = np.fft.fftfreq(N, d=1/framerate)[:max]
            for l in range(int((cent.shape[0] - N)/s)):
                data = cent[l*s:l*s+N]

                ave = np.mean(data)
                data = data-ave
                data = data*window

                spec = np.fft.fft(data)[:max]
                ampList.append(np.abs(spec))
            time = np.arange(0, l+1, 1) * s / framerate
            ampList = np.array(ampList)

            ampMean = np.mean(ampList, axis = 0)


            #df_amp = pd.DataFrame(data=ampList, index=time, columns=freq)

            
            axs1[j].plot(freq, np.log10(ampMean), label=pitch[k], linewidth=0.8)
        #ax1.set_xscale("log")
        axs1[j].set_xlim(0,100)
        axs1[j].set_ylim(-0.5,3.5)
        axs1[j].grid(which='major',color='grey',linestyle='-')
        axs1[j].grid(which='minor',color='grey',linestyle='-')
        axs1[j].text(20,0.2,"/"+vowels[j]+"/")
        axs1[j].set_xlabel("Frequency",fontsize=8)
        axs1[j].set_ylabel("Power",fontsize=8)
        axs1[j].legend(fontsize=6)
                

            
        '''
            sns.heatmap(data=np.log10(df_amp.iloc[:, :100].T), 
            xticklabels=100, 
            yticklabels=50, 
            cmap=plt.cm.inferno,
            cbar=False,
            ax=axs2[k]
            )
            #axs2[k].set_ylim(0,200)

            axs1[k].plot(range(cent.shape[0]), cent, linewidth=0.8)
            axs1[k].set_xlim(0,6000)
            axs1[k].set_xticks(range(0,6001,1000), minor=False)
            axs1[k].set_xticklabels(range(1,8,1))
            
            #fig.suptitle(str(i+1)+"_"+vowels[j])

            #plt.show()
            '''
    #fig.suptitle(str(i+1))
    plt.tight_layout()
    plt.savefig("long_spectrogram_"+str(i+1)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.cla()
'''         
            ax1 = fig.add_subplot(411)
            ax2 = fig.add_subplot(412)
            ax3 = fig.add_subplot(413)
            ax4 = fig.add_subplot(414)
            axs = [ax1, ax2, ax3, ax4]



    for key in range(4):
        filename =  "1/long/1_" +vowel+ "_" + str(key+1)
        fname = "wav_analysis/data/F0_1ms/" +filename+ ".txt"
        f0 = np.loadtxt(fname, delimiter=',')
        cent = 1200*np.log2(f0/pitch_Hz[key])

        axs[key].plot(time, cent)


        graph_fix(axs[key])
    

'''

    #plt.legend()

    