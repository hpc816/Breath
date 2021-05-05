

from flask import Blueprint, request, jsonify


app_upload=Blueprint('app_upload',__name__)



import os
import sys

from flask import Flask
from . import app_upload

sys.path.append('../../../')



@app_upload.route('/<type>/<username>',methods=['POST'])
def upload(type,username):
    '''
    视图函数用于接受用户在小程序端上传的文件，并保存到指定位置
    :param type: 呼吸类型，sniff/deep
    :param username:用户名
    :return:
    '''
    if request.method == 'POST':
        f_obj = request.files.get('wav')
        if f_obj is None:
            return "未上传文件"

        try:


            save_link = '../../data/'+type + '/'+username

            isExists_sniff = os.path.exists(save_link)
            if not (isExists_sniff):


                os.makedirs(save_link)
            save_path = save_link


            FileList = []
            FileNames = os.listdir(save_path)
            if len(FileNames) > 0:
                for fn in FileNames:

                    fullfilename = os.path.join(save_path, fn)
                    FileList.append(fullfilename)

                if len(FileList) > 0:
                    FileList.sort()
            num = len(FileList)


            save_file = save_path + './sniff' + str(num) + '.wav'




            f_obj.save(save_file)
        except Exception as e:
            print(e)
            return jsonify(uploadcode=333,detail='文件上传失败')
        else:
            return jsonify(uploadcode=666,detail='文件上传成功.保存路径为'+os.path.abspath(save_file),filepath=os.path.abspath(save_file))












