


import sys

from flask import Flask, render_template, request, json

sys.path.append('../../')

import os
from model import test2

app = Flask(__name__)



@app.route('/verification_sniff')
def verification_sniff():

    file_wav_test = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    save_path = '基本目录/test/sniff' + '用户的身份'
    save_file_test = save_path + '/sniff.wav'
    f = open(save_file_test, "wb")
    data = file_wav_test.read()
    f.write(data)
    f.close()




    featype = 'gfcc'
    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'

    count = 0
    verif_count = 0





    predict = test2.task_predict(save_path, outmodel, featype)


    flag = test2.task_Verify(save_path, outmodel, featype, '用户身份')



    if predict == '用户身份' and flag:
        result = 'True'
        save_link_deep = '基本目录/sniff' + '用户的身份'

        FileList = []
        FileNames = os.listdir(save_link_deep)
        if len(FileNames) > 0:
            for fn in FileNames:

                fullfilename = os.path.join(save_link_deep, fn)
                FileList.append(fullfilename)

            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)

        save_file = save_link_deep + '/sniff' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav_test.read()
        f.write(data)
        f.close()


        input_dir = r'\基本目录\sniff\*'
        test2.task_enroll(input_dir, outmodel, featype)
    else:
        result = 'False'

    os.remove(save_file_test)

    return render_template('index.html')


@app.route('/verification_deep')
def verification_deep():

    file_wav_test = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    save_path = '基本目录/test/deep' + '用户的身份'
    save_file_test = save_path + '/deep.wav'
    f = open(save_file_test, "wb")
    data = file_wav_test.read()
    f.write(data)
    f.close()




    featype = 'gfcc'
    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'

    count = 0
    verif_count = 0





    predict = test2.task_predict(save_path, outmodel, featype)


    flag = test2.task_Verify(save_path, outmodel, featype, '用户身份')



    if predict == '用户身份' and flag:
        result = 'True'
        save_link_deep = '基本目录/deep' + '用户的身份'

        FileList = []
        FileNames = os.listdir(save_link_deep)
        if len(FileNames) > 0:
            for fn in FileNames:

                fullfilename = os.path.join(save_link_deep, fn)
                FileList.append(fullfilename)

            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)

        save_file = save_link_deep + '/deep' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav_test.read()
        f.write(data)
        f.close()


        input_dir = r'\基本目录\deep\*'
        test2.task_enroll(input_dir, outmodel, featype)
    else:
        result = 'False'

    os.remove(save_file_test)

    return render_template('index.html')



@app.route("/collection_deep", methods=["POST"])
def collection_deep():
    file_wav = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    if file_wav:


        save_link_sniff = '基本目录/sniff' + '用户的身份'
        save_link_deep = '基本目录/deep' + '用户的身份'

        isExists_sniff = os.path.exists(save_link_sniff)
        isExists_deep = os.path.exists(save_link_deep)
        if not (isExists_sniff and isExists_deep):


            os.makedirs(save_link_sniff)
            os.makedirs(save_link_deep)
        save_path = save_link_deep

        FileList = []
        FileNames = os.listdir(save_path)
        if len(FileNames) > 0:
            for fn in FileNames:

                fullfilename = os.path.join(save_path, fn)
                FileList.append(fullfilename)

            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)

        save_file = save_path + '/deep' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav.read()
        f.write(data)
        f.close()




    featype = 'gfcc'



    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'




    input_dir = r'\基本目录\deep\*'
    test2.task_enroll(input_dir, outmodel, featype)


@app.route("/collection_sniff", methods=["POST"])
def collection_sniff():
    file_wav = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    if file_wav:


        save_link_sniff = '基本目录/sniff' + '用户的身份'
        save_link_deep = '基本目录/deep' + '用户的身份'

        isExists_sniff = os.path.exists(save_link_sniff)
        isExists_deep = os.path.exists(save_link_deep)
        if not (isExists_sniff and isExists_deep):


            os.makedirs(save_link_sniff)
            os.makedirs(save_link_deep)
        save_path = save_link_sniff

        FileList = []
        FileNames = os.listdir(save_path)
        if len(FileNames) > 0:
            for fn in FileNames:

                fullfilename = os.path.join(save_path, fn)
                FileList.append(fullfilename)

            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)

        save_file = save_path + '/sniff' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav.read()
        f.write(data)
        f.close()



        name = os.listdir("\\flask/data\\test")
        featype = 'gfcc'



        outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'

        pwd = os.path.abspath(os.path.join(os.getcwd(), ".."))


        input_dir = pwd + r'\基本目录\deep\*'
        test2.task_enroll(input_dir, outmodel, featype)
























    if __name__ == '__main__':
        app.run(debug=True)












































