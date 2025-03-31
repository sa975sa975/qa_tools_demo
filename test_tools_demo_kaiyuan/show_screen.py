# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tkinter import *
import tkinter as tk

logConfMap = {
    "info": {
        "foreground": "green",
        "tag": "INFO"
    },
    "warn": {
        "foreground": "orange",
        "tag": "WARN"
    },
    "error": {
        "foreground": "red",
        "tag": "ERROR"
    }
}

# 处理窗口尺寸
def center_window(window: tk.Tk, width, height, rel_x, rel_y):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - int(width * rel_x)
    y = (screen_height // 2) - int(height * rel_y)

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# 创建子窗口
def set_kid_screen(screen: tk.Tk, title='执行结果'):
    # 打开新窗口显示结果
    kid_screen = Toplevel(screen, bg='white')
    kid_screen_width = 400
    kid_screen_height = 240
    center_window(kid_screen, kid_screen_width, kid_screen_height, 0.5, 0.5)
    kid_screen.title(title)
    kid_screen.grab_set()  # 阻止与主窗口的交互，直到弹窗关闭
    kid_screen.focus_set()  # 设置焦点在弹窗上
    return kid_screen, kid_screen_width, kid_screen_height


class ShowScreen():

    def __init__(self, screen: tk.Tk, title: str):
        self.screen = screen
        self.screen.title(title)
        self.test_env_str = ""
        self.config_version = ""
        self.test_uid_list = []
        # 是否选择了游戏包
        self.package_is_choosed = False
        # 用于存储uid 和 uid列表的数据
        self.test_uid_list_1 = []
        self.test_uid_list_2 = []
        # 存储参数的字典
        self.input_args_dict = {}
        self.building_level = 0
        self.kid_screen = None
        # 判断能否继续进行方法
        self.need_init = True
        # 额外的标识信息
        self.extra_info = ""

        # 设置窗口大小
        self.screen_width = 640
        self.screen_height = 320
        center_window(self.screen, self.screen_width, self.screen_height, 0.5, 0.5)

