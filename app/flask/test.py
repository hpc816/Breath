# coding=utf8


import sys

from flask import Flask, render_template, request, json
from db import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get_wav", methods=["POST"])
def get_wav():
    # JSON包形式传入
    input_voice = str(json.loads(request.values.get("voice")))
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
