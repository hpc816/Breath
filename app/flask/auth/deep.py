import os
import sys

from flask import Flask
from . import app_auth

sys.path.append('../../../') #将根目录Breath引入导包路径
from model.test2 import task_Verify

@app_auth.route('deep')
def auth_deep():
    return 'auth_deep'