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
def task_enroll(input_dir, output_model,featype='mfcc1'):
    '''
    :输入文件目录，训练得到模型
    :param input_dir: 文件目录
    :param output_model:输出模型【传入的是一个文件名】
    :param featype:使用的特征向量类型
        mfcc1:通过speech实现的MFCC，维度：
        mfcc2:通过spafe实现的MFCC，维度：
        gfcc:通过spafe实现的GFCC，维度：
        plp：通过spafe实现的PLP，维度：
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
    print(dirs)

    # 处理特殊情况
    if (len(dirs) == 0):
        print("%s目录下没有文件夹，退出执行" % input_dir)
        sys.exit(1)  # 异常退出

    # 迭代目录，进行标签绑定
    for d in dirs:  # 每个文件目录代表一个用户
        label = os.path.basename(d.rstrip('/'))  # 标签绑定
        # print(label)
        wavs = glob.glob(d + "/*.wav")  # 指定读取wav格式的文件
        print(wavs)
        if len(wavs) == 0:
            print("%s中没有.wav文件" % d)
            continue
        for wav in wavs:  # 读取wav文件，并对每个文件进行特征提取
            try:
                # wavfile读取.wav音频
                y, sr = read_wav(wav)
                # 获取mfcc feature,并加入字典中
                model.enroll(label, y, sr,featype)  # 进行特征提取，并以name作为键值，将特征储存到特征字典中
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
    y, sr = li.load(fname,sr=16000)
    if len(y.shape)!=1: #若不是单声道，就把它转换为单声道
        print("convert stereo to mono")
        y=y[:,0]

    return y, sr


def task_predict(input_files,input_model,featype):
    '''
    预测输入文件在给定模型下的分类结果
    :param input_file: 输入的测试文件列表
    :param input_model: 训练好的模型文件
    :param featype:特征向量类型
    :return: 输入文件在给定模型下的预测结果【标签，以用户名形式返回】
    '''
    model=GMMModel.load(input_model) #载入模型
    for f in glob.glob(input_files): #加载测试文件
        #读取wav文件
        y,sr=read_wav(f)
        #使用predict预测
        label,score,all_scores=model.predict(y,sr,featype)
        print(f,'->',label,',score->',score,'all scores(without softmax)->',all_scores)
    return label



def task_Verify(input_files,input_model,featype,label):
    '''
    验证输入文件是否是对应的用户
    :param input_file: 输入的测试文件列表
    :param input_model: 训练好的模型文件
    :param featype:特征向量类型
    :param label:输入测试文件的类别
    :return: 验证结果
    '''
    model=GMMModel.load(input_model) #载入模型
    for f in glob.glob(input_files): #加载测试文件
        #读取wav文件
        y,sr=read_wav(f)
        # Verify
        flag = model.Verify(y, sr, featype,label)
        if flag == True:
            print(f, '->', '验证通过')
        else:
            print(f, '->', '验证失败')
    return  flag


if __name__ == "__main__":
    featype='gfcc' #提取的特征向量类型
    outmodel='gmm_model_'+featype+'.out' #输出模型的路径

    #获取上级目录
    # pwd=os.path.abspath(os.path.join(os.getcwd(), ".."))
    #  #通过上级目录定位到训练集数据目录
    # input_dir=pwd+r'\data\normal\*'
    # task_enroll(input_dir, outmodel,featype)

    #测试部分
    name = ['hpc', 'yfk','hhc']
    count = 0
    verif_count=0
    total = 0
    for i in range(len(name)):
        # path = "./test/" + name[i]
        path = r"C:\Users\hpc\Desktop\Breath\data\test/" + name[i]
        for file in os.listdir(path):
            print(path + "/" + file)
            total += 1.0  # 记录音频测试样本总数
            predict = task_predict(path + "/" + file, outmodel,featype)  # 使用之前训练好的模型进行测试
            if (predict == name[i]):
                count += 1  # 预测对了的测试样本数+1
            flag=task_Verify(path + "/" + file, outmodel,featype,name[i])
            if(flag):
                verif_count+=1 #验证对了的测试样本数+1


    print("Predict accuracy：", count / total,'Verification accuracy:',verif_count/total)  # 打印预测的准确率
