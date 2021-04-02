# 本模块构建GMM模型
import pickle
import time
from collections import defaultdict

import numpy as np
from sklearn.mixture import GaussianMixture  # 导入高斯混合模型包
import math
import operator

from model.features import MFCC


class GMMSet:  # GMM集合，每个GMM代表一个用户【或一种对象】
    def __init__(self, gmm_order=32):
        '''
        初始化GMM模型【设置一些参数】
        :param gmm_order:GMM中高斯分布的数量，这里默认设置为13 [需要保证n_samples（MFCC维数） >= n_components]
        :param covariance_type: 协方差矩阵样式，默认设置为对角矩阵
        '''
        self.gmms = []  # GMM列表，每个元素是一个高斯混合模型
        self.gmm_order = gmm_order  # 模型中高斯分布的数量
        # self.covariance_type=covariance_type  #模型协方差矩阵样式
        self.y = []  # 标签列表【一共有几类，每一类由用户名代表的标签表示】

    def fit_new(self, x, label):
        '''
        根据输入特征向量和标签，得到一个混合高斯分布模型，而后将新得到的模型加入gmms列表中
        :param x: 输入的特征（用于训练）
        :param label:标签
        :return:gmms中新增一个GMM
        '''
        self.y.append(label)
        # 下面不知道为什么，协方差矩阵用对角矩阵diag型就不行
        gmm = GaussianMixture(self.gmm_order, covariance_type='diag')  # 初始化一个高斯混合模型类，这里设置高斯分布数量为32，协方差矩阵为对角矩阵
        gmm.fit(x)  # 根据输入的特征向量，使用EM算法估算模型参数,返回训练后的模型
        self.gmms.append(gmm)  # 将得到的高斯混合模型加入模型集合

    def gmm_score(self, gmm, x):
        '''
        计算模型得分
        :param gmm:  高斯混合模型
        :param x: 用于测试的特征向量矩阵
        :return: 计算得分【把x中每一个特征向量的得分加起来作为最后的得分】
        '''
        return np.sum(gmm.score(x))  # gmm.scroe返回一个列表，列表中每个元素是X的一个特征向量的得分，np.sum()计算列表元素的和，作位最终结果返回

    @staticmethod  # 静态方法，只是名义上归属类管理，但是不能使用类变量和实例变量，是类的工具包
    def softmax(scores):
        '''
        分类器，使用softmax函数进行计算每个类别的“概率”【softmax的作用就是将得分映射到0-1之前，类似于概率的形式】
        :param scores:对于每一个输入的X，GMMSet会调用gmm_score计算出特定gmm模型下的得分，多个gmm模型得到一个scores列表
        :return: 最大概率占总体的比重
        '''
        scores_sum = sum([math.exp(i) for i in scores])
        score_max = math.exp(max(scores))  # 取出最大得分作为e的指数
        return round(score_max / (scores_sum), 3)  # round() 方法返回浮点数x的四舍五入值【3表示保留小数点后三位】

    def predict_one(self, x):
        '''
        预测类别
        :param x:输入的音频特征向量
        :return: 返回类别（用户名/姓名。。）和评分
        '''
        scores = [self.gmm_score(gmm, x) / len(x) for gmm in self.gmms]  # 获取每个人gmm评分的【均值】
        # p = sorted(enumerate(scores), key=operator.itemgetter(1), reverse=True)#根据gmm评分排序
        # p = [(str(self.y[i]), y, p[0][1] - y) for i, y in p]
        result = [(self.y[index], value) for (index, value) in
                  enumerate(scores)]  # 用标签取代scores中的index，每个标签代表一个用户，用户有其自己的GMM模型
        p = max(result, key=operator.itemgetter(1))  # 获取评分最大值
        # 【operator.itemgetter()：返回一个可调用对象，用于从运算对象中获取元素】，括号里面的1表示选择result中的第二项，即分数项
        softmax_score = self.softmax(scores)  # 映射为0-1之间
        return p[0], softmax_score  # 返回姓名和评分

    def before_pickle(self):  # 使用pickle保存模型之前
        pass

    def after_pickle(self):  # 使用pickle保存模型之后
        pass


class GMMModel:
    def __init__(self):
        '''
        features:特征向量字典，键为用户名，值为特征向量矩阵
        gmmset:GMM模型组
        '''
        self.features = defaultdict(list)  # 当字典的key不存在时，返回的是[],即一个空的列表
        self.gmmset = GMMSet()  # 获取GMM模型组

    def enroll(self, name, y, sr):
        '''
        对输入音频进行特征提取，而后以键值对的方式加入features字典中
        :param name:标签【用户名/姓名】
        :param y:音频时间序列
        :param sr:采样率
        '''
        feat = np.array(MFCC(y, sr))  # 提取MFCC特征,并转换为np数组
        self.features[name].extend(feat)  # 加入字典

    def train(self):
        '''
        模型训练
        '''
        self.gmmset = GMMSet()  # 实例化一个GMM模型组对象，用于下面的训练过程
        start_time = time.time()  # 开始时间  time.time()：返回当前时间的时间戳（1970纪元后经过的浮点秒数）
        for name, feats in self.features.items():  # 迭代特征向量字典
            try:
                self.gmmset.fit_new(np.array(feats), name)  # 对每一个用户，训练出一个GMM模型后，加入到GMM模型组中
            except Exception as e:
                print("%s failed %s" % (name, e))  # 打印处理那个用户时发生了错误
        print(time.time() - start_time, " seconds")  # 打印训练所需的时间

    def predict(self, y, sr):
        '''
        进行预测
        :param y:输入音频的时间序列
        :param sr: 采样率
        :return: 预测的标签【用户名/姓名】、评分
        '''
        try:
            feat = MFCC(y, sr)
        except Exception as e:
            print(e)
        return self.gmmset.predict_one(feat)

    def save(self, fname):
        '''
        保存训练好的模型
        :param fanme: 保存模型的文件名
        '''
        # 使用pickle模块
        with open(fname, 'wb') as f:  # 写入模型
            pickle.dump(self, f, -1)
        # 使用

    def load(fname):
        '''
        加载训练好的模型
        fname:文件名
        :return:返回模型
        '''
        with open(fname, 'rb') as f:  # 以只读方式打开文件
            M = pickle.load(f)  # 加载之前保存的模型
            return M
