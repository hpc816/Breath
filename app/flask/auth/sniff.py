import os
import sys

from flask import Flask
from . import app_auth

sys.path.append('../../../')
from model.test2 import task_Verify

@app_auth.route('sniff')
def auth_sniff():
    return 'auth_sniff'

