
import json

from flask import Blueprint, request, jsonify
from .intersection import intersection



app_friend=Blueprint('app_friend',__name__)


@app_friend.route('/',methods=['POST','GET'])
def index():
    data=request.get_data()
    my_json=json.loads(data)
    set1=my_json.get('set1')
    set2=my_json.get('set2')

    ret= intersection(set1,set2)
    ret=list(ret.intersection(ret))
    ret=','.join(ret)


    return jsonify(intersection=ret)
