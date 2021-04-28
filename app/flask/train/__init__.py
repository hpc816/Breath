#本模块用于训练模型

from flask import Blueprint, jsonify
from model.test2 import task_enroll

#创建一个蓝图
app_train=Blueprint('app_train',__name__)

#在__init__.py被执行时，把视图加载进来，让蓝图和应用程序知道有视图的存在

import os
import sys
import time

from flask import Flask
from . import app_train

sys.path.append('../../../') #将根目录Breath引入导包路径
from model.test2 import task_enroll


@app_train.route('/<type>',methods=['POST','GET'])
def train(type):
    '''
    视图函数根据URL中的呼吸类型和用户名，寻找到音频文件存放目录，而后训练出UserModel和OthersModel，
    并保存到指定的路径
    初步先考虑一次性使用目录下所有音频文件进行模型训练【整体训练】
    而后再考虑对单个用户训练出自己的UserModel和OthersModel
    :param type:呼吸类型
    #:param username:用户名
    :return:训练结果（状态码+描述字符串），模型文件保存的路径
    '''
    input_dir= '../../data/'+type  #训练音频文件目录的路径
    output_model_path='../../model/models'+'/'+type #训练得到模型文件的保存目录路径
    t = time.time()
    output_model = output_model_path + '/' + str(t) + '.out'  # 输出模型文件文件路径


    # 判断是否存在该用户的文件夹
    isExists_input = os.path.exists(input_dir)
    isExists_output=os.path.exists(output_model_path)
    if not (isExists_input):
        # 不存在则创建该目录
        os.makedirs(input_dir)
    if not (isExists_output):
        # 不存在则创建该目录
        os.makedirs(output_model_path)

    #进行模型训练
    #超参数设置
    modeltype='gmm_model' #模型类型
    featype='gfcc1' #提取的特征向量类型
    verifytype='GMM_type2' #验证类型：GMM_type1:逐帧比较； GMM_type2:相邻帧比较； GMM_type3:整体比较
    gmmorder=6 #GMM超参数
    refined=False #Login时是否对音频文件进行提纯操作

    try:
        task_enroll(input_dir+'/*', output_model, featype, gmmorder, refined)
    except Exception as e:#打印错误信息
        print(e)
        return jsonify(traincode=333, detail='模型训练失败')
    else:#训练成功
        #返回JSON数据
        return jsonify(traincode=666,detail='模型训练成功')

