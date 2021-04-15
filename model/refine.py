# 本模块用于对原始音频文件进行提纯处理
import time

import numpy as np
import librosa as li
import librosa.display as lid
from matplotlib import  pyplot as plt


# 音频文件预处理
def refine(y, sr):
    '''
    :param y: 需要提纯的音频时间序列
    :param sr: 音频采样率
    :return: y_n: 提纯之后的音频时间序列
    '''
    # 利用短时能量+汉明窗口提纯音频（过滤掉静默音和背景音）
    frame_size = 0.02  # 每帧为0.02s,对应0.02*sample_rate个采样点
    frame_size = int(frame_size * sr)  # 将时间转换为样本点数
    y_n = []
    y_e = []
    k = 0
    for i in range(0, len(y), frame_size):
        y_e.append(float(0))
        for j in range(i, i + frame_size - 1):  # 计算一个帧里的能量作为第i点的能量值
            if (j >= len(y)):
                break
            else:
                y_e[k] += y[j] * y[j] * (0.54 - 0.46 * np.cos((2 * np.pi * j) / (frame_size - 1)))  # 加上一个汉明窗口，使变化更加平滑
        k += 1
    k = 0
    for i in range(0, len(y), frame_size):
        if (y_e[k] > 0.003):
            for j in range(i, i + frame_size):
                if (j >= len(y)):
                    break
                else:
                    y_n.append(y[j])
        k += 1
    y_n = np.array(y_n)
    return y_n

if __name__=="__main__":
    y, sr = li.load(r'C:\Users\hpc\Desktop\Breath\data\normal\hpc\正常呼吸3.wav', sr=None, duration=20)

    start_time=time.time()
    y_n=refine(y,sr)

    print('refine操作所需时间：',time.time()-start_time)
    # plt.figure()
    # plt.subplot(2,1,1)
    # lid.waveplot(y,sr)
    # plt.title(' wavform')
    #
    # plt.subplot(2,1,2)
    # lid.waveplot(y_n,sr)
    # plt.title(' wavform_energy')
    # plt.tight_layout() #保证图不重叠#
    # plt.show()