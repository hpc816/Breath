#本模块用于接收上传的数据，并放到指定的位置

from flask import Blueprint, request, jsonify

#创建一个蓝图
app_upload=Blueprint('app_upload',__name__)

#在__init__.py被执行时，把视图加载进来，让蓝图和应用程序知道有视图的存在

import os
import sys

from flask import Flask
from . import app_upload

sys.path.append('../../../') #将根目录Breath引入导包路径



@app_upload.route('/<type>/<username>',methods=['POST'])
def upload(type,username):
    '''
    视图函数用于接受用户在小程序端上传的文件，并保存到指定位置
    :param type: 呼吸类型，sniff/deep
    :param username:用户名
    :return:
    '''
    if request.method == 'POST':
        f_obj = request.files.get('w')  # 返回一个文件对象，里面传入的键值时请求时的参数名，而不是文件名
        if f_obj is None:
            return "未上传文件"

        try:
            # 存储路径
            # 基本目录写死
            save_link = '../../data/'+type + '/'+username
            # 判断是否存在该用户的文件夹
            isExists_sniff = os.path.exists(save_link)
            if not (isExists_sniff):
                # 不存在则创建该目录
                # os.makedirs(save_link)
                os.makedirs(save_link)
            save_path = save_link

            # 文件名编号
            FileList = []
            FileNames = os.listdir(save_path)
            if len(FileNames) > 0:
                for fn in FileNames:
                    # 默认直接返回所有文件名
                    fullfilename = os.path.join(save_path, fn)
                    FileList.append(fullfilename)
                # 对文件名排序
                if len(FileList) > 0:
                    FileList.sort()
            num = len(FileList)

            # 存储时的文件名
            save_file = save_path + './sniff' + str(num) + '.wav'
            # f = open(save_file, "wb")
            # data = f_obj.read()
            # f.write(data)
            # f.close()
            f_obj.save(save_file)
        except Exception as e:
            print(e)
            return jsonify(uploadcode=333,detail='文件上传失败')
        else:
            return jsonify(uploadcode=666,detail='文件上传成功.保存路径为'+os.path.abspath(save_file),filepath=os.path.abspath(save_file))




# isExists_sniff = os.path.exists('././././')
# path=os.getcwd()
# path=os.path.abspath(os.path.join(os.getcwd(), "../../../data"))
# print(path+'/y.wav')

# path=os.path.abspath('../../../data/sniff' + '/hpc')
# # print(path)

