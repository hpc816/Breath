
import json
import os

from flask import Blueprint, request, redirect, jsonify


app_auth=Blueprint('app_auth',__name__)


from .sniff import auth_sniff
from .deep import auth_deep
from model.test2 import task_Verify
from model.test2 import task_predict


@app_auth.route('/<type>/<username>',methods=['POST'])
def auth(type,username):
    '''h
    视图函数接收呼吸类型和用户名，从本地获取已经训练好的模型（根据目录进行获取），进行验证
    :param type: 呼吸类型，sniff/deep
    :param username:用户名
    :return: json类型，包括认证结果代码和描述字符串等
    '''


    data = request.get_data()
    data = json.loads(data)
    filepath = data['filepath']


    featype = 'gfcc1'
    verifytype = 'GMM_type2'

    gmmorder = 6
    refined = True


    model_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + '/model'

    data_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    if type == 'deep':
        input_path = data_path + '/data/deep/*'
    elif type == 'sniff':
        input_path = data_path + '/data/sniff/*'


    input_model_path = model_path + r'/models/' + str(type)
    FileList = []
    FileNames = os.listdir(input_model_path)
    if len(FileNames) > 0:
        for fn in FileNames:

            fullfilename = os.path.join(input_model_path, fn)
            FileList.append(fullfilename)

        if len(FileList) > 0:
            FileList.sort()
    num = len(FileList)-1



    input_model = input_model_path + '/' + str(type) + str(num) + '.out'




    predict = task_predict(filepath, input_model, featype)
    flag =task_Verify(filepath, input_model,username,featype, verifytype)
    if predict == username and flag:
        result = 'True'

        return jsonify(authcode=000, detail='认证成功')
    else:
        result = 'False'
        os.remove(filepath)
        return jsonify(authcode=100, detail='认证失败')


