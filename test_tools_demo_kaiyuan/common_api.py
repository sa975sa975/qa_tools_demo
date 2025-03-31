# -*- coding:utf-8 -*-
import os, sys

import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import functools
import logging
import time
import requests



class MatchConditions:
    """
    概述:
        任务条件装饰器,用于决定当前任务是否符合可执行条件。
        注意@task装饰器必须在条件装饰器的上方。
    参数:
        conditions (dict): 条件键值对字典,注意里面的值是布尔类型
        gid (int): 用户gid
    
    用法1:
        @task
        def init_task(self):
            @MatchConditions({'need_init_task': self.need_init_task}, self.gid)
            def init_task():
                self.init()
            init_task()
    用法2(如果要判断的变量不是布尔类型,可以通过使用条件判断语句将其转换为布尔类型):
        @task
        def init_task(self):
            @MatchConditions({'not need_init_task': self.need_init_task == False, 'condition_1 not empty': len(self.condition_1) != 0, 'local_task_type': self.task_type == 1}, self.gid)
            def init_task():
                self.init()
            init_task()
    """
    def __init__(self, conditions: dict, gid: int):
        self.conditions = conditions
        self.gid = gid
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            if all(self.conditions.values()):
                return func(*args, **kwargs)
            else:
                not_match_conditions_list = [i for i in self.conditions if not self.conditions[i]]
                logging.debug(f'for the following items {str(not_match_conditions_list)} not match the conditions, user {str(self.gid)} will not run {str(func.__name__)}')
        return wrapped_function
    
def get_op_time():
    op_time = int(round(time.time() * 1000))
    return op_time

def get_response(method, protocol, host, path, headers, data, port=80):
    if host in ['xxx-xxx-xxx.xxx.com', 'xxx-xxx-xxx.xxx.cn']:
        port = 0000
    url = f'{protocol}://{host}:{port}{path}'
    response = requests.request(method, url, headers=headers, data=data)
    return response



