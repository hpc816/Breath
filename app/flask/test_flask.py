# coding=utf8


import sys

from flask import Flask, render_template, request, json

sys.path.append('../../') #将根目录Breath引入导包路径

import os
from model import test2

app = Flask(__name__)


# 身份验证工作
@app.route('/verification_sniff')
def verification_sniff():
    # 保存test文件
    file_wav_test = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    save_path = '基本目录/test/sniff' + '用户的身份'
    save_file_test = save_path + '/sniff.wav'
    f = open(save_file_test, "wb")
    data = file_wav_test.read()
    f.write(data)
    f.close()

    # 测试部分
    # name = ['hpc', 'yfk', 'hhc']
    # name = os.listdir("\\flask/data\\test")
    featype = 'gfcc'  # 提取的特征向量类型
    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'  # 输出模型的路径
    # print(name)
    count = 0
    verif_count = 0
    # for i in range(len(name)):
    # path = "./test/" + name[i]
    # path = r"D:\Github_Desktop\BreathPrint\data\test/"
    # for file in os.listdir(path):
    # print(path + "/" + file)
    predict = test2.task_predict(save_path, outmodel, featype)  # 使用之前训练好的模型进行测试
    # if predict == name[i]:
    # count += 1  # 预测对了的测试样本数+1
    flag = test2.task_Verify(save_path, outmodel, featype, '用户身份')
    # if flag:
    # verif_count += 1  # 验证对了的测试样本数+1

    if predict == '用户身份' and flag:
        result = 'True'
        save_link_deep = '基本目录/sniff' + '用户的身份'
        # 文件名编号
        FileList = []
        FileNames = os.listdir(save_link_deep)
        if len(FileNames) > 0:
            for fn in FileNames:
                # 默认直接返回所有文件名
                fullfilename = os.path.join(save_link_deep, fn)
                FileList.append(fullfilename)
            # 对文件名排序
            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)
        # 存储时的文件名
        save_file = save_link_deep + '/sniff' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav_test.read()
        f.write(data)
        f.close()

        # 重新训练模型
        input_dir = r'\基本目录\sniff\*'
        test2.task_enroll(input_dir, outmodel, featype)
    else:
        result = 'False'

    os.remove(save_file_test)

    return render_template('index.html')


@app.route('/verification_deep')
def verification_deep():
    # 保存test文件
    file_wav_test = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    save_path = '基本目录/test/deep' + '用户的身份'
    save_file_test = save_path + '/deep.wav'
    f = open(save_file_test, "wb")
    data = file_wav_test.read()
    f.write(data)
    f.close()

    # 测试部分
    # name = ['hpc', 'yfk', 'hhc']
    # name = os.listdir("\\flask/data\\test")
    featype = 'gfcc'  # 提取的特征向量类型
    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'  # 输出模型的路径
    # print(name)
    count = 0
    verif_count = 0
    # for i in range(len(name)):
    # path = "./test/" + name[i]
    # path = r"D:\Github_Desktop\BreathPrint\data\test/"
    # for file in os.listdir(path):
    # print(path + "/" + file)
    predict = test2.task_predict(save_path, outmodel, featype)  # 使用之前训练好的模型进行测试
    # if predict == name[i]:
    # count += 1  # 预测对了的测试样本数+1
    flag = test2.task_Verify(save_path, outmodel, featype, '用户身份')
    # if flag:
    # verif_count += 1  # 验证对了的测试样本数+1

    if predict == '用户身份' and flag:
        result = 'True'
        save_link_deep = '基本目录/deep' + '用户的身份'
        # 文件名编号
        FileList = []
        FileNames = os.listdir(save_link_deep)
        if len(FileNames) > 0:
            for fn in FileNames:
                # 默认直接返回所有文件名
                fullfilename = os.path.join(save_link_deep, fn)
                FileList.append(fullfilename)
            # 对文件名排序
            if len(FileList) > 0:
                FileList.sort()
        num = len(FileList)
        # 存储时的文件名
        save_file = save_link_deep + '/deep' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav_test.read()
        f.write(data)
        f.close()

        # 重新训练模型
        input_dir = r'\基本目录\deep\*'
        test2.task_enroll(input_dir, outmodel, featype)
    else:
        result = 'False'

    os.remove(save_file_test)

    return render_template('index.html')


# 数据的采集工作
@app.route("/collection_deep", methods=["POST"])
def collection_deep():
    file_wav = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    if file_wav:
        # 存储路径
        # 基本目录写死
        save_link_sniff = '基本目录/sniff' + '用户的身份'
        save_link_deep = '基本目录/deep' + '用户的身份'
        # 判断是否存在该用户的文件夹
        isExists_sniff = os.path.exists(save_link_sniff)
        isExists_deep = os.path.exists(save_link_deep)
        if not (isExists_sniff and isExists_deep):
            # 不存在则创建该目录
            # os.makedirs(save_link)
            os.makedirs(save_link_sniff)
            os.makedirs(save_link_deep)
        save_path = save_link_deep
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
        save_file = save_path + '/deep' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav.read()
        f.write(data)
        f.close()

    # 模型重新训练
    # name = ['hpc', 'yfk', 'hhc']
    # name = os.listdir("\\flask/data\\test")
    featype = 'gfcc'  # 提取的特征向量类型
    # type1:逐帧比较
    # type2:相邻帧比较
    # type3：直接比较
    outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'  # 输出模型的路径
    # 获取上级目录
    # pwd = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # 通过上级目录定位到训练集数据目录
    # input_dir = pwd + r'\data\deep\*'
    input_dir = r'\基本目录\deep\*'
    test2.task_enroll(input_dir, outmodel, featype)


@app.route("/collection_sniff", methods=["POST"])
def collection_sniff():
    file_wav = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    if file_wav:
        # 存储路径
        # 基本目录写死
        save_link_sniff = '基本目录/sniff' + '用户的身份'
        save_link_deep = '基本目录/deep' + '用户的身份'
        # 判断是否存在该用户的文件夹
        isExists_sniff = os.path.exists(save_link_sniff)
        isExists_deep = os.path.exists(save_link_deep)
        if not (isExists_sniff and isExists_deep):
            # 不存在则创建该目录
            # os.makedirs(save_link)
            os.makedirs(save_link_sniff)
            os.makedirs(save_link_deep)
        save_path = save_link_sniff
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
        save_file = save_path + '/sniff' + str(num) + '.wav'
        f = open(save_file, "wb")
        data = file_wav.read()
        f.write(data)
        f.close()

        # 模型重新训练
        # name = ['hpc', 'yfk', 'hhc']
        name = os.listdir("\\flask/data\\test")
        featype = 'gfcc'  # 提取的特征向量类型
        # type1:逐帧比较
        # type2:相邻帧比较
        # type3：直接比较
        outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'  # 输出模型的路径
        # 获取上级目录
        pwd = os.path.abspath(os.path.join(os.getcwd(), ".."))
        # 通过上级目录定位到训练集数据目录
        # input_dir = pwd + r'\data\deep\*'
        input_dir = pwd + r'\基本目录\deep\*'
        test2.task_enroll(input_dir, outmodel, featype)

    # JSON包形式传入
    # input_voice = str(json.loads(request.values.get("voice")))

    # 保存音频信息到本地文件夹
    # 如果无法直接传输过来WAV格式的话转一下格式
    # import os
    #
    # m4a_path = "/Users/Downloads/start1/"
    # m4a_file = os.listdir(m4a_path)
    # for i, m4a in enumerate(m4a_file):
    # os.system("ffmpeg -i "+ m4a_path + m4a + " " + m4a_path + str(i) + ".wav" )
    # ffmpeg 可以用来处理视频和音频文件，可以设置一些参数，如采样频率等

    # 保存文件到本地目录
    # from urllib import request
    # 需要保存的文件即Wav
    # save_link = ''
    # 调用request类中的urlretrieve()方法实现保存图片到指定文件夹下
    # path 处填入路径名与文件名
    # request.urlretrieve(save_link, path='.wav')

    # 下面接到test2里面的main函数部分？

    if __name__ == '__main__':
        app.run(debug=True)

# 是否需要数据库？数据库存储什么？提前构建数据库
# score_db=db('mysql数据库ip地址',3306,'数据库用户名','数据库密码','数据库','utf8')
# conn=score_db.connect_db()
# cursor=conn.cursor()
# 需要进行的sql语句的处理？
# sql = " "
# cursor.execute(sql)
# res=cursor.rowcount
# conn.commit()
# cursor.close()
# conn.close()
# if res == 1:
# print res
# res = '数据提交成功'
# return json.dumps(res.decode('utf8'))
# else:
# print(res)
# res = '数据提交失败'
# return json.dumps(res.decode('utf8'))

# 查看后端数据库有无该用户先前的信息

# 如果有则根据JSON包判断是需要进行验证还是需要进行重新训练
# 还需要判断验证与训练的呼吸方式为2选1 sniff/deep
# 如果没有则保存用户的信息

# score_db=db('mysql数据库ip地址',3306,'数据库用户名','数据库密码','数据库','utf8')
# conn=score_db.connect_db()
# cursor=conn.cursor()
# 需要进行的sql语句的处理？
# sql = " "
# 1.查询该用户是否首次使用 先前是否有其信息
# select * from table名 where 信息(user='' and password='')
# 2.插入首次使用的用户的账号信息
# insert into table名 信息('user','password')
# 3.找出该用户的对应信息 用作与训练后结果比对 身份验证
# select * from table名 where 信息(user='' and password='') 本质同1一样
# 4......
# cursor.execute(sql)
# res=cursor.rowcount
# conn.commit()
# cursor.close()
# conn.close()
