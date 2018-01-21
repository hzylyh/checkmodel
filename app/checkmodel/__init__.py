#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Hou

from flask import Blueprint

checkmodel = Blueprint("checkmodel", __name__)

import app.checkmodel.views