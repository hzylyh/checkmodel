#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Hou

from flask import Flask
from app.checkmodel import checkmodel

app = Flask(__name__)


app.register_blueprint(checkmodel)