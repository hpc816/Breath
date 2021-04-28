#本模块用于进行认证
import os

from flask import Blueprint, request, redirect

#创建一个蓝图
app_auth=Blueprint('app_auth',__name__)

#在__init__.py被执行时，把视图加载进来，让蓝图和应用程序知道有视图的存在
from .sniff import auth_sniff
from .deep import auth_deep
from model.test2 import task_Verify



@app_auth.route('/<type>/<username>',methods=['POST','GET'])
def auth(type,username):
    '''
    视图函数接收呼吸类型和用户名，从本地获取已经训练好的模型（根据目录进行获取），进行验证
    :param type: 呼吸类型，sniff/deep
    :param username:用户名
    :return: json类型，包括认证结果代码和描述字符串等
    '''
    # 保存test文件
    # file_wav_test = request.files.get('发送文件的包名：应该包括了用户的身份 如名字简写')
    # save_path = '基本目录/test/sniff' + '用户的身份'
    # save_file_test = save_path + '/sniff.wav'
    # f = open(save_file_test, "wb")
    # data = file_wav_test.read()
    # f.write(data)
    # f.close()
    #调用upload API，进行文件接收和本地保存
    dic=redirect('http://127.0.0.1:5000/upload/type/username')
    #print(dic)
    return redirect('http://127.0.0.1:5000/upload/'+type+'/'+username)
    # # 测试部分
    # # name = ['hpc', 'yfk', 'hhc']
    # # name = os.listdir("\\flask/data\\test")
    # featype = 'gfcc'  # 提取的特征向量类型
    # outmodel = 'gmm_model_' + featype + "GMM_type2_30" + '.out'  # 输出模型的路径
    # # print(name)
    # count = 0
    # verif_count = 0
    # # for i in range(len(name)):
    # # path = "./test/" + name[i]
    # # path = r"D:\Github_Desktop\BreathPrint\data\test/"
    # # for file in os.listdir(path):
    # # print(path + "/" + file)
    # predict = test2.task_predict(save_path, outmodel, featype)  # 使用之前训练好的模型进行测试
    # # if predict == name[i]:
    # # count += 1  # 预测对了的测试样本数+1
    # flag = test2.task_Verify(save_path, outmodel, featype, '用户身份')
    # # if flag:
    # # verif_count += 1  # 验证对了的测试样本数+1
    #
    # if predict == '用户身份' and flag:
    #     result = 'True'
    #     save_link_deep = '基本目录/sniff' + '用户的身份'
    #     # 文件名编号
    #     FileList = []
    #     FileNames = os.listdir(save_link_deep)
    #     if len(FileNames) > 0:
    #         for fn in FileNames:
    #             # 默认直接返回所有文件名
    #             fullfilename = os.path.join(save_link_deep, fn)
    #             FileList.append(fullfilename)
    #         # 对文件名排序
    #         if len(FileList) > 0:
    #             FileList.sort()
    #     num = len(FileList)
    #     # 存储时的文件名
    #     save_file = save_link_deep + '/sniff' + str(num) + '.wav'
    #     f = open(save_file, "wb")
    #     data = file_wav_test.read()
    #     f.write(data)
    #     f.close()
    #
    #     # 重新训练模型
    #     input_dir = r'\基本目录\sniff\*'
    #     task_enroll(input_dir, outmodel, featype)
    # else:
    #     result = 'False'
    #
    # os.remove(save_file_test)
    #
    # return '认证完成'
