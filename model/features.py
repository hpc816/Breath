# 本模块用于提取音频信号的特征向量
import sys
import librosa as li
import librosa.display as lid
from python_speech_features import mfcc, delta, base

###########################################################
import scipy.io.wavfile
import scipy

from spafe.utils import vis
import spafe.features.mfcc as spfm
from spafe.features.gfcc import gfcc
from spafe.features.rplp import plp
from spafe.features.bfcc import bfcc
from spafe.features.lfcc import lfcc
from spafe.features.lpc import lpcc
from spafe.features.msrcc import msrcc
from spafe.features.ngcc import ngcc
from spafe.features.pncc import pncc
from spafe.features.psrcc import psrcc


# 音频文件特征提取【MFCC】
def MFCC(y, sr):
    '''
    :param y:输入音频时间序列
    :param sr: 输入音频采样率
    :return: 输入音频的mfcc特征向量
    '''

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
    #mfcc_feature = li.feature.mfcc(y=y, sr=sr, n_mfcc=39)
    mfcc_feature=mfcc(y,sr)
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


def MFCC2(y,sr):
    mfcc_feature = spfm.mfcc(y, sr)

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
    # gfcc_feature = mfcc(sig, 13)
    # spafe.features.gfcc.gfcc(sig,  #单声道音频时间序列（Nx1）
    #                          fs=16000, #采样率，默认设置为16000
    #                          num_ceps=13,  #返回的倒谱数维度，默认为13
    #                          pre_emph=0, #如果为1，则应用预强调。默认值为1
    #                          pre_emph_coeff=0.97, #    #pre_emph_coeff=0.97, #
    #                          win_len=0.025, #窗口长度（秒）。默认值为0.025
    #                          win_hop=0.01, #以秒为单位在连续窗口之间移动。默认值为0.01
    #                          win_type='hamming',  #应用的窗口类型，默认为汉明窗口
    #                          nfilts=40, #滤波器组的个数，默认为40
    #                          nfft=512, #一次FFT的样本点数，默认为512
    #                          low_freq=None,  #滤波器最低频率值，默认为0
    #                          high_freq=None,  #滤波器最高频率值，默认为采样率/2
    #                          scale='constant',
    #                          dct_type=2,
    #                          use_energy=False,
    #                          lifter=22,
    #                          normalize=1)
    gfcc_feature=gfcc(y,sr,num_ceps=32,nfilts=40)

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
    #函数原型
    #spafe.features.rplp.plp(sig, fs, num_ceps=13, pre_emph=0,
    # pre_emph_coeff=0.97, win_len=0.025, win_hop=0.01,
    # modelorder=13, normalize=0）
    plp_feature = plp(y, sr)

    if len(plp_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return plp_feature



def BFCC(y,sr):
    #spafe.features.bfcc.bfcc(sig, fs=16000, num_ceps=13,pre_emph=0,
    # pre_emph_coeff=0.97,win_len=0.025,  win_hop=0.01,win_type='hamming',
    # nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant',dct_type=2, use_energy=False, lifter=22, normalize=1
    bfcc_feature = bfcc(y, sr)

    if len(bfcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return bfcc_feature


def LFCC(y,sr):
    #spafe.features.lfcc.lfcc(sig, fs=16000, num_ceps=13, pre_emph=0,
    # pre_emph_coeff=0.97, win_len=0.025, win_hop=0.01, win_type='hamming',
    # nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant', dct_type=2,
    # use_energy=False, lifter=22, normalize=1)

    lfcc_feature = lfcc(y, sr)

    if len(lfcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return lfcc_feature


def LPCC(y,sr):
  #  spafe.features.lpc.lpcc(sig, fs=16000, num_ceps=13, pre_emph=1,
  #  pre_emph_coeff=0.97, win_type='hann', win_len=0.025,
#  win_hop=0.01, do_rasta=True, lifter=1, normalize=1, dither=1)
    lpcc_feature = lpcc(y, sr)

    if len(lpcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return lpcc_feature



def MSRCC(y,sr):
    #spafe.features.msrcc.msrcc(sig, fs=16000, num_ceps=13, pre_emph=0,
# pre_emph_coeff=0.97, win_len=0.025, win_hop=0.01, win_type='hamming',
# nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant',
# gamma=-0.14285714285714285, dct_type=2, use_energy=False, lifter=22, normalize=1)
    msrcc_feature = msrcc(y, sr)

    if len(msrcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return msrcc_feature


def NGCC(y,sr):
    #spafe.features.ngcc.ngcc(sig, fs=16000, num_ceps=13, pre_emph=0,
# pre_emph_coeff=0.97, win_len=0.025, win_hop=0.01, win_type='hamming',
# nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant',
# dct_type=2, use_energy=False, lifter=22, normalize=1)
    ngcc_feature = ngcc(y, sr)

    if len(ngcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return ngcc_feature


def PNCC(y,sr):
    #spafe.features.pncc.pncc(sig, fs=16000, num_ceps=13, pre_emph=0,
# pre_emph_coeff=0.97, power=2, win_len=0.025, win_hop=0.01, win_type='hamming',
# nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant', dct_type=2,
# use_energy=False, dither=1, lifter=22, normalize=1)
    pncc_feature = pncc(y, sr)

    if len(pncc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return pncc_feature


def PSRCC(y,sr):
#spafe.features.psrcc.psrcc(sig, fs=16000, num_ceps=13, pre_emph=0,
# pre_emph_coeff=0.97, win_len=0.025, win_hop=0.01, win_type='hamming',
# nfilts=26, nfft=512, low_freq=None, high_freq=None, scale='constant',
# gamma=-0.14285714285714285, dct_type=2, use_energy=False,
# lifter=22, normalize=1)
    psrcc_feature = psrcc(y, sr)

    if len(psrcc_feature) == 0:
        print >> sys.stderr, "ERROR.. failed to extract mfcc feature:", len(y)

    return psrcc_feature


def ShowAll(y,sr):
    print('python_speech_features mfcc特征')
    mfccs = MFCC(y, sr)
    print(mfccs)
    print(mfccs.shape)

    print('spafe mfcc特征')
    mfccs2 = MFCC2(y, sr)
    print(mfccs2)
    print(mfccs2.shape)

    print('spafe gfcc特征')
    gfccs = GFCC(y, sr)
    print(gfccs)
    print(gfccs.shape)

    print('spafe plp特征')
    plps = PLP(y, sr)
    print(plps)
    print(plps.shape)

    print('spafe bfcc特征')
    bfccs = BFCC(y, sr)
    print(bfccs)
    print(bfccs.shape)

    print('spafe lfcc特征')
    lfccs = LFCC(y, sr)
    print(lfccs)
    print(lfccs.shape)

    print('spafe lpcc特征')
    lpccs = LPCC(y, sr)
    print(lpccs)
    print(lpccs.shape)

    #MSRCC特征运行起来会报错
    # print('spafe msrcc特征')
    # msrccs = MSRCC(y, sr)
    # print(msrccs)
    # print(msrccs.shape)

    print('spafe ngcc特征')
    ngccs = NGCC(y, sr)
    print(ngccs)
    print(ngccs.shape)

    print('spafe pncc特征')
    pnccs = PNCC(y, sr)
    print(pnccs)
    print(pnccs.shape)

    #PSRCC特征运行起来会报错
    # print('spafe psrcc特征')
    # psrccs = PSRCC(y, sr)
    # print(psrccs)
    # print(psrccs.shape)


if __name__ == "__main__":
    #################################
    # init input vars
    num_ceps = 13
    low_freq = 0
    high_freq = 2000
    nfilts = 24
    nfft = 512
    dct_type = 2,
    use_energy = False,
    lifter = 5
    normalize = False
    #########################################
    input = r'C:\Users\hpc\Desktop\Breath\data\normal\hpc\正常呼吸5.wav'
    fs, sig = scipy.io.wavfile.read(input)
    y, sr = li.load(input,sr=16000)
    # print("librosa:")
    # print(y)
    # print("-------------------")
    # print(sr)
    # mfcc_li = MFCC(y, sr)
    # print(mfcc_li)
    ##############################
    # print("spafe:")
    # print(fs)
    # print("-------------------")
    # print(sig)
    ShowAll(y,sr)


