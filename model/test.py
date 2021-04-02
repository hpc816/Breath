# 本模块用于测试
import glob
import itertools
import os
import librosa as li
import librosa.display as lid
from matplotlib import pyplot as plt
import sys
from model.gmm import GMMModel


# 读取文件并训练
def task_enroll(input_dir, output_model):
    '''
    :输入文件目录，训练得到模型
    :param input_dir: 文件目录
    :param output_model:输出模型【传入的是一个文件名】
    :return
    '''
    # 初始化GMM模型
    model = GMMModel()

    # 清除空格换行符
    input_dir = input_dir.strip().split()
    # print(input_dir)

    # 创造目录迭代器，读取子目录【各个用户的音频文件目录】
    dirs = itertools.chain(*(glob.glob(d) for d in input_dir))
    dirs = [d for d in dirs if os.path.isdir(d)]
    # 打印出来的为用户文件夹清单——用户清单
    print(dirs)

    # 处理特殊情况
    # 当所扫描的目录下没有文件夹的时候
    if (len(dirs) == 0):
        print("%s目录下没有文件夹，退出执行" % input_dir)
        sys.exit(1)  # 异常退出

    # 迭代目录，进行标签绑定
    # 遍历list 处理读入的每一个音频文件夹——用户
    for d in dirs:  # 每个文件目录代表一个用户
        label = os.path.basename(d.rstrip('/'))  # 标签绑定
        # 打印出来的为当前处理的用户名/标识
        # print(label)
        wavs = glob.glob(d + "/*.wav")  # 指定读取wav格式的文件
        # 打印出当前用户在目录下所采集到的所有的声音样本
        print(wavs)
        # 无样本时 取下一个用户
        if len(wavs) == 0:
            print("%s中没有.wav文件" % d)
            continue
        # 有样本 读取wav音频文件
        for wav in wavs:  # 读取wav文件，并对每个文件进行特征提取
            try:
                # wavfile读取.wav音频
                y, sr = read_wav(wav)
                # 获取mfcc feature,并加入字典中
                model.enroll(label, y, sr)  # 进行特征提取，并以name作为键值，将特征储存到特征字典中
                print("wav %s ready" % (wav))
            except Exception as e:
                print(wav + " error %s" % (e))
    # 训练GMM模型组
    model.train()
    # 保存训练好的模型
    model.save(output_model)


def read_wav(fname):
    '''
    读取文件，通过librosa或scipy.io.wavfile来实现
    :param fname: 文件路径
    :return:
        y:音频时间序列
        sr:音频采样率
    '''
    y, sr = li.load(fname)

    return y, sr


if __name__ == "__main__":
    input_dir = r'D:\Github_Desktop\BreathPrint\data\normal\*'
    # test_dir=r'C:\Users\hpc\Desktop\BreathPrint\data\test\*'
    task_enroll(input_dir, 'gmm_test_model.out')
