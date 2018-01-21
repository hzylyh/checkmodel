#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Hou

from flask import render_template
from . import checkmodel


@checkmodel.route("/index")
def index():
    return render_template("checkmodel/index.html")