import json
import os
import sys

from flask import Flask, jsonify, request
from . import app_auth

sys.path.append('../../../')
from model.test2 import task_Verify
from model.test2 import task_predict



@app_auth.route('deep/<username>', methods=['POST', 'GET'])
def auth_deep(username):

    data = request.form.get('data')
    data = json.loads(data)
    filepath = data['filepath']

    featype = 'gfcc'

    outmodel = r'C:\Users\hpc\Desktop\Breath\model\models\sniff\1619690355.4103081.out'

    predict = task_predict(filepath, outmodel, featype)
    flag =task_Verify(filepath, outmodel, featype, username)
    if predict == username and flag:
        result = 'True'

        return jsonify(uploadcode=000, detail='认证成功')
    else:
        result = 'False'
        os.remove(filepath)
        return jsonify(uploadcode=100, detail='认证失败')