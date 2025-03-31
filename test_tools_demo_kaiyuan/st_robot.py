# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import logging
from pathlib import Path
main_path = Path(os.path.realpath(__file__)).parent
sys.path.append(r'{}'.format(main_path))

from simplejson import JSONDecodeError
from common_api import MatchConditions

from st_config import *
import tkinter as tk
from tkinter import *

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(funcName)s] %(message)s")


# 初始化属性
class StTaskSet:
    def __init__(self):
        pass

    def init_task_set(self, uid: int):
        self.count: int = 0
        self.uid = uid

# 调用方法
class TestRobot(StTaskSet):
    def __init__(self, uid, judge_res=set(), test_env=None):
        self.uid = uid
        self.judge_res = judge_res
        self.test_env = test_env if test_env else HOST
    
    # 测试调用api
    def test_func_1(self):
        # 装饰器函数, 满足条件后执行
        # @MatchConditions({"inited": not self.need_init, "manifested": not self.need_manifest}, self.uid)
        def test_func_1():
            """
            此处调用api接口
            # try:
            #     res_json = requests.request(method, url, headers=headers, data=data).json()
            # except (JSONDecodeError) as e:
            #     logging.info(f'{self.uid} test_func_1 fail, error info: {e}')
            """
            try:
                print("Hello, this is the location to call the test api")
                self.judge_res.add("Hello, this is the location to call the test api")
            except (JSONDecodeError, TypeError) as e:
                logging.info(f'{self.uid} test_func_1 fail, error info: {e}')
                self.judge_res.add("test_func_1")
            return self.judge_res
        return test_func_1()
        

