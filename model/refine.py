#本模块用于对原始音频文件进行提纯处理
import numpy as np

#音频文件预处理
def refine(y,sr):
    '''
    :param y: 需要提纯的音频时间序列
    :param sr: 音频采样率
    :return: y_n: 提纯之后的音频时间序列
    '''
    # 利用短时能量+汉明窗口提纯音频（过滤掉静默音和背景音）
    frame_size=0.02 #每帧为0.02s,对应0.02*sample_rate个采样点
    frame_size=int(frame_size*sr) #将时间转换为样本点数
    y_n=[]

    y_e=[]
    k=0
    for i in range(0,len(y),frame_size):
        y_e.append(float(0))
        for j in range(i,i+frame_size-1):#计算一个帧里的能量作为第i点的能量值
            if(j>=len(y)):
                break
            else:
                y_e[k]+=y[j]*y[j]*(0.54 - 0.46 * np.cos((2 * np.pi * j) /(frame_size - 1)))#加上一个汉明窗口，使变化更加平滑
        k += 1

    k=0
    for i in range(0,len(y),frame_size):
        if(y_e[k]>0.003):
            for j in range(i,i+frame_size):
                if(j>=len(y)):
                    break
                else:
                    y_n.append(y[j])
        k+=1

    y_n=np.array(y_n)
    return y_n