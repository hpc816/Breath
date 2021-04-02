# 本模块用于提取音频信号的特征向量
import sys
import librosa as li
import numpy as np
import librosa.display as lid
# from python_speech_features import mfcc, delta, base

###########################################################
import scipy.io.wavfile
import scipy
from spafe.utils import vis
from spafe.features.mfcc import mfcc
from spafe.features.gfcc import gfcc


# 音频文件特征提取【MFCC】
def MFCC(y, sr):
    '''
    :param y:输入音频时间序列
    :param sr: 输入音频采样率
    :return: 输入音频的mfcc特征向量
    '''
    # spafe
    mfcc_feature = mfcc(y,sr)

    # 1.librosa.feature.mfcc  【重要】
    # 函数原型：librosa.feature.mfcc(y=None, sr=22050, S=None, n_mfcc=20, dct_type=2, norm='ortho', **kwargs)
    # 参数介绍：y：音频时间序列，np.ndarray [shape=(n,)] 或 None
    #         sr: y的采样率 number > 0 [scalar]
    #          S:对数功能梅尔谱图 np.ndarray [shape=(d, t)] or None
    #          n_mfcc:要返回的MFCC数量  int > 0 [scalar]
    #          dct_type:离散余弦变换（DCT）类型。默认情况下，使用DCT类型2 None, or {1, 2, 3}
    #          norm:规范。如果dct_type为2或3，则设置norm =’ortho’使用正交DCT基础。 None or ‘ortho’
    #           【 标准化不支持dct_type = 1。】
    #          kwargs:额外的关键参数 【参数melspectrogram，如果按时间序列输入操作】
    #          返回： MFCC序列 M:np.ndarray [shape=(n_mfcc, t)]  【？】
    # mfcc_feature = li.feature.mfcc(y=y, sr=sr, n_mfcc=39)

    # 2.from python_speech_features import mfcc
    # mfcc_feature = mfcc(wavedata, framerate, winlen=0.064, winstep=0.032, nfilt=13, nfft=1024)  # mfcc系数
    # 其中wavedata为语音数据
    # framerate为采样率
    # winlen为帧长，单位为秒
    # winstep为帧移，单位为秒
    # nfilt为返回的mfcc数据维数，默认为13维（但经过我的实验，nfilt最多也只能返回13维的mfcc参数）
    # nfft为fft点数，一般要和帧长对应的采样点数要一样
    # mfcc_feature=mfcc(y,sr)
    # 获取39维的MFCC特征
    # wav_feature = mfcc(y, sr)
    # d_mfcc_feat = delta(wav_feature, 1)
    # d_mfcc_feat2 = delta(wav_feature, 2)
    # mfcc_feature = np.hstack((wav_feature, d_mfcc_feat, d_mfcc_feat2))

    # 异常处理
    if len(mfcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return mfcc_feature


# 音频文件特征提取【GFCC】
def GFCC(y, sr):
    '''
    提取输入文件的GFCC特征
    :param y:输入音频时间序列
    :param sr: 输入音频采样率
    :return: GFCC特征向量
    '''
    # spafe库能否实现gfcc？
    gfcc_feature = gfcc(y, sr)
    # 参数列表：
    # sig (array)：一种单声道音频信号（Nx1），用于计算特征
    # fs (int)：正在处理信号的采样率 默认值为 16000_________
    # num_ceps (float)：要返回的倒谱数 默认值为13_________
    # pre_emph (int)：如果为1，则应用预强调。默认值为1_________
    # pre_emph_coeff (float):应用预加重过滤器[1-预加重]（0=无）
    # win_len (float):窗口长度（秒）。默认值为0.025_________
    # win_hop (float):以秒为单位在连续窗口之间移动。默认值为0.01。_________
    # win_type (float):窗口类型以应用窗口。默认值为“hamming”。_________
    # nfilts (int):过滤器组中过滤器的数量。默认值为40。_________
    # nfft (int):FFT点数。默认值为512。_________
    # low_freq (int):mel滤波器的最低频带边缘（Hz）。默认值为0。_________
    # high_freq (int):mel滤波器的最高频带边缘（Hz）。默认值为samplerate/2=8000。_________
    # scale (str):选择最大bin振幅是上升、下降还是恒定（=1） 默认为恒定_________
    # dct_type(int):使用的DCT类型-1或2（HTK为3，feac为4）。默认值为2。_________
    # use_energy (int):用真对数能量覆盖C0默认值为0_________
    # lifter (int):如果值>0，则应用提升,默认值为22_________
    # normalize (int):如果为1,则应用规范化,默认值为0_________
    if len(gfcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract gfcc feature:", len(y)
    return gfcc_feature


# 音频文件特征提取【plp】
def PLP(y, sr):
    '''
    提取输入音频文件的PLP特征
    :param y:输入音频时间序列
    :param sr: 输入音频采样率
    :return: PLP特征向量
    '''
    pass


if __name__ == "__main__":
    input = r'D:\Github_Desktop\BreathPrint\data\normal\hpc\正常呼吸3.wav'
    y, sr = li.load(input,sr=16000)
    print("librosa:")
    print(y)
    print("-------------------")
    print(sr)
    gfcc = GFCC(y, sr)
    print(gfcc)

