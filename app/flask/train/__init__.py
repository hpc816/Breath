

from flask import Blueprint, jsonify
from model.test2 import task_enroll


app_train=Blueprint('app_train',__name__)



import os
import sys
import time

from flask import Flask
from . import app_train

sys.path.append('../../../')
from model.test2 import task_enroll


@app_train.route('/<type>',methods=['POST','GET'])
def train(type):
    '''
    视图函数根据URL中的呼吸类型和用户名，寻找到音频文件存放目录，而后训练出UserModel和OthersModel，
    并保存到指定的路径
    初步先考虑一次性使用目录下所有音频文件进行模型训练【整体训练】
    而后再考虑对单个用户训练出自己的UserModel和OthersModel
    :param type:呼吸类型

    :return:训练结果（状态码+描述字符串），模型文件保存的路径
    '''
    input_dir= '../../data/'+type
    output_model_path='../../model/models'+'/'+type


    isExists_input = os.path.exists(input_dir)
    isExists_output=os.path.exists(output_model_path)
    if not (isExists_input):

        os.makedirs(input_dir)
    if not (isExists_output):

        os.makedirs(output_model_path)



    FileList = []
    FileNames = os.listdir(output_model_path)
    if len(FileNames) > 0:
        for fn in FileNames:

            fullfilename = os.path.join(output_model_path, fn)
            FileList.append(fullfilename)

        if len(FileList) > 0:
            FileList.sort()
    num = len(FileList)


    output_model = output_model_path + '/' + str(type) + str(num) + '.out'





    modeltype='gmm_model'
    featype='gfcc1'
    verifytype='GMM_type2'
    gmmorder=6
    refined=False

    try:
        task_enroll(input_dir+'/*', output_model, featype, gmmorder, refined)
    except Exception as e:
        print(e)
        return jsonify(traincode=100, detail='模型训练失败')
    else:

        return jsonify(traincode=000,detail='模型训练成功')

