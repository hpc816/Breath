# 本模块用于测试
import glob
import itertools
import os
import pickle
import time
from collections import defaultdict

import librosa as li
import librosa.display as lid
from matplotlib import pyplot as plt
import sys
import numpy as np
from pathlib import Path


from model.gmm import GMMModel
from model.features import extraction
from model.refine import refine

# 读取文件并训练
def task_enroll(input_dir, output_model,featype,gmmorder,refined=False):
    '''
    :输入文件目录，训练得到模型
    :param input_dir: 文件目录
    :param output_model:输出模型【传入的是一个文件名】
    :param featype:使用的特征向量类型
        mfcc1:通过speech实现的MFCC，维度：
        mfcc2:通过spafe实现的MFCC，维度：
        gfcc1:通过spafe实现的GFCC，维度：32
        gfcc2:通过spafe实现的GFCC，维度：96
        plp：通过spafe实现的PLP，维度：
    :param gmm_order:GMM模型超参数
    :param refined:是否进行提纯操作
    :return
    '''
    # 初始化GMM模型
    model = GMMModel(gmmorder)

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

                # 是否需要提纯，若为True，则进行提纯操作
                if refined:
                    y=refine(y, sr)

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



def task_Verify(input_files,input_model,label,featype,verifytype):
    '''
    验证输入文件是否是对应的用户
    :param input_file: 输入的测试文件列表
    :param input_model: 训练好的模型文件
    :param label:输入测试文件的类别
    :param featype:特征向量类型
    :param verifytype:验证类型
    :return: 验证结果
    '''
    model=GMMModel.load(input_model) #载入模型
    for f in glob.glob(input_files): #加载测试文件
        #读取wav文件
        y,sr=read_wav(f)
        # Verify
        flag = model.Verify(y, sr, label,featype,verifytype)
        if flag == True:
            print(f, '->', '验证通过')
        else:
            print(f, '->', '验证失败')
        return  flag


def task_login(input_dir,featype,refined=False):
    '''
    输入文件目录，进性提纯（可选）、特征提取，并将提取到的特征保存到指定路径
    :param input_dir: 文件目录
    :param featype: 特征向量类型
        mfcc1:通过speech实现的MFCC，维度：
        mfcc2:通过spafe实现的MFCC，维度：
        gfcc1:通过spafe实现的GFCC，维度：32
        gfcc2:通过spafe实现的GFCC，维度：96
        plp：通过spafe实现的PLP，维度：
    :param refined: 是否对输入的原始音频文件进行提纯操作，缺省为不进行
    :return:特征向量文件的路径
    '''
    feat_dir=Path(input_dir[:-1]+featype)
    #print(feat_dir)
    try:
        if os.path.exists(feat_dir):#目录已存在，读取目录即可
            print('目录已存在')
        else:#目录不存在，需要新建一个目录，并完成音频文件的提纯、提取特征向量等操作
            os.mkdir(feat_dir)

        # 声明一个字典，保存用户：特征向量矩阵
        features = defaultdict(list)  # 当字典的key不存在时，返回的是[],即一个空的列表

        # 清除空格换行符
        input_dir = input_dir.strip().split()
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

                    #是否需要提纯，若为True，则进行提纯操作
                    if refined:
                        y=refine(y,sr)

                    # 提取特征向量
                    feat = np.array(extraction(featype, y, sr))

                    # 将特征向量放入字典
                    features[label].extend(feat)  # 加入字典
                    print("wav %s ready" % (wav))
                except Exception as e:
                    print(wav + " error %s" % (e))
        # 保存特征向量字典

        #fname = str(feat_dir) + '/' + time.asctime(time.localtime(time.time())) + '.feat'
        if refined==True:
            fname=str(feat_dir) + '\\refined\\' + str(round(time.time())) + '.feat'
        fname = str(feat_dir) + '\\' + str(round(time.time())) + '.feat'

        with open(fname, 'wb') as f:  # 将特征向量字典写入文件
            pickle.dump(features, f, -1)
            return fname  # 返回特征向量文件的路径

    except Exception as e:
        print(e)




def task_logout(fname,gmm_order,output_model):
    '''
    从保存的文件中读取特征向量，然后进行模型的训练
    :param fname: 保存特征向量字典的文件路径
    :param gmm_order :GMM超参数
    :param output_model: 训练得到的模型保存的文件路径
    :return: 训练好的模型
    '''
    with open(fname, 'rb') as f:  # 以只读方式打开文件
        Feat_dic = pickle.load(f)  # 加载之前保存的特征向量字典

    # 初始化GMM模型
    model = GMMModel()
    #enroll
    for name,feat in Feat_dic.items():
        model.features[name].extend(feat)  # 加入字典

    #train
    model.train()

    # 保存训练好的模型
    model.save(output_model)

    return model


def test(outmodel,verifytype,featype,refined=False):
    '''使用测试集测试模型预测的准确率以及验证通过率
    :param outmodel:已经训练好的模型
    :param featype:提取的特征类型
    :param verifytye:验证类型
    :param refined:是否进行提纯操作
    '''
    #测试部分
    #name = ['hpc', 'yfk','hhc']
    # 获取测试文件目录
    twd = pwd + r'\data\test'
    name = os.listdir(twd)
    print(name)
    count = 0
    verif_count=0
    total = 0
    for i in range(len(name)):
        # path = "./test/" + name[i]
        path = twd+'//' + name[i]
        for file in os.listdir(path):
            print(path + "/" + file)
            total += 1.0  # 记录音频测试样本总数
            predict = task_predict(path + "/" + file, outmodel,featype)  # 使用之前训练好的模型进行测试
            if (predict == name[i]):
                count += 1  # 预测对了的测试样本数+1
            flag=task_Verify(path + "/" + file, outmodel,name[i],featype,verifytype)
            if(flag):
                verif_count+=1 #验证对了的测试样本数+1


    print("Predict accuracy：", count / total,'Verification accuracy:',verif_count/total)  # 打印预测的准确率



if __name__ == "__main__":
    #超参数设置
    modeltype='gmm_model' #模型类型
    featype='gfcc1' #提取的特征向量类型
    verifytype='GMM_type2' #验证类型：GMM_type1:逐帧比较； GMM_type2:相邻帧比较； GMM_type3:整体比较
    gmmorder=6 #GMM超参数
    refined=False #Login时是否对音频文件进行提纯操作

    #获取上级目录
    pwd=os.path.abspath(os.path.join(os.getcwd(), ".."))
    #  #通过上级目录定位到训练集数据目录
    input_dir=pwd+r'\data\normal\*' #训练集数据的路径
    model_dir=pwd+r'\model\models\*' #模型文件的保存路径

    #输出模型文件名，详情见/model/models/说明.md命名规范
    outmodel_enroll=model_dir[:-1]+modeltype+'_'+featype+'_'+verifytype+'_'+str(gmmorder)+'.out' #输出模型的路径
    outmodel_logout=model_dir[:-1]+modeltype+'_'+featype+'_'+verifytype+'_'+str(gmmorder)+'_'+str(refined)+'.out'
    # print(outmodel_enroll)
    # print(outmodel_logout)



    # #测试enroll\predict\Verify
    task_enroll(input_dir, outmodel_enroll,featype,gmmorder,refined)

    # #测试Login和Logout
    # #feat_file=task_login(input_dir,featype,refined)
    # feat_file=pwd+r'\data\normal\gfcc\1617594937.feat' #特征向量文件的路径
    # model=task_logout(feat_file,outmodel_logout)
    test(outmodel_enroll,verifytype,featype)