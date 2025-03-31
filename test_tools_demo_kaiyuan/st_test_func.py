# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

"""
此模块用于图形化界面调用具体项目的函数方法
"""

from gevent import monkey
monkey.patch_all()

import sys
import os
from pathlib import Path

from st_gevent_concurrent_api import concurrent_uid_requests
from st_robot import TestRobot


""" Debug Function """
# 1.test_func_1_1
def test_func_1_1(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 2.test_func_1_2
def test_func_1_2(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 3.test_func_1_3
def test_func_1_3(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 4.test_func_1_4
def test_func_1_4(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 5.test_func_2_1
def test_func_2_1(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 6.test_func_2_2
def test_func_2_2(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 6.test_func_2_2
def test_func_2_2(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 7.test_func_2_3
def test_func_2_3(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 8.test_func_3_1
def test_func_3_1(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 9.test_func_3_2
def test_func_3_2(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res

# 10.test_func_4_1
def test_func_4_1(test_env, test_uid_list):
    def func_1(uid: int, judge_res, test_env):
        nonlocal res
        test_robot = TestRobot(uid, judge_res, test_env)
        res = test_robot.test_func_1()
    res = set()
    concurrent_uid_requests(func_1, test_uid_list, 5, res, test_env)
    return res