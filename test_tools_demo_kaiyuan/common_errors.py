# -*- coding:utf-8 -*-
# 异常捕捉 #

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class TestLossParamsError(Exception):
    pass