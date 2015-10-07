# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)
app.secret_key='123&DF#lx90@dxL'

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.from_pyfile('settings.py')

from . import views


