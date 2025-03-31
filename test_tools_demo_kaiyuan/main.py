# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from show_screen import ShowScreen, set_kid_screen
from st_test_func import *
from st_config import *
from verify import get_entry_env, get_entry_uid_list, get_entry_parama_1, get_entry_parama_2
import st_config_change

if sys.platform == 'win32':
    from tkinter import Button as Button_test
elif sys.platform == 'darwin':
    import tkmacosx
    from tkmacosx import Button as Button_test
else:
    Button_test = None


# 通过字符串执行方法
def call_fun_by_str(fun_str, *args):
    return eval(fun_str)(*args)


class TestStoolsDemo(ShowScreen):
    def __init__(self, screen: tk.Tk, title: str):
        super().__init__(screen, title)

    # 初始启动方法
    def load_all_func(self):
        """1.设置测试环境 和 Uid"""
        # 点击后全选输入框的内容
        def select_all_1(event):
            entry1.select_range(0, "end")
        def select_all_2(event):
            entry2.select_range(0, "end")
        def check_entry_env(event):
            if "master" in entry1.get() or "dev" in entry1.get() or "release" in entry1.get():
                self.test_env_str = get_entry_env(entry1.get())
                if self.test_env_str == "":
                    entry1.delete(0, "end")
                    entry1.insert(0, "如: master, dev-xxx")
                    entry1.config(fg="grey")
                else:
                    entry1.config(fg="black")
                    # print(self.test_env_str)
            else:
                self.test_env_str == ""
                entry1.delete(0, "end")
                entry1.insert(0, "如: master, dev-xxx")
                entry1.config(fg="grey")

        # 检查客户端版本号
        def check_config_version(event):
            if "." in entry2.get() and entry2.get()[0].isdigit() and entry2.get()[-1].isdigit and "".join(entry2.get().split(".")).isdigit() and len(entry2.get().split(".")) == 3:
                entry2.config(fg="black")
                client_version = entry2.get()
                # st_config.py中更新客户端版本号
                st_config_change.get_new_client_version(client_version)
            else:
                entry2.delete(0, "end")
                entry2.insert(0, f"{st_config_change.CLIENT_VERSION_OLD}(当前默认)")
                entry2.config(fg="grey")
                # st_config.py中更新客户端版本号
                st_config_change.get_new_client_version(st_config_change.CLIENT_VERSION_OLD)

        # 单选按钮
        def on_check():
            # 获取当前选中的复选框
            if self.var1.get() != self.var1_old.get() and self.var1.get() == 1:
                self.var2.set(0)
                self.var3.set(0)
            elif self.var2.get() != self.var2_old.get() and self.var2.get() == 1:
                self.var1.set(0)
                self.var3.set(0)
            elif self.var3.get() != self.var3_old.get() and self.var3.get() == 1:
                self.var1.set(0)
                self.var2.set(0)
            # 保存数据
            self.var1_old.set(self.var1.get())
            self.var2_old.set(self.var2.get())
            self.var3_old.set(self.var3.get())
            if self.var1_old.get() or self.var2_old.get() or self.var3_old.get():
                self.package_is_choosed = True
            else:
                self.package_is_choosed = False
            # print(self.var1_old.get())
            # print(self.var2_old.get())
            # print(self.var3_old.get())
            # print(self.package_is_choosed)
                
            # 更新渠道
            # manifest
            if self.var1.get() == 1:
                st_config_change.get_new_project("test_channel_a")
            elif self.var2.get() == 1:
                st_config_change.get_new_project("test_channel_b")
            elif self.var3.get() == 1:
                st_config_change.get_new_project("test_channel_c")

        # 输入测试环境 和 Uid
        self.frame1 = Frame(self.screen, height=0.2*self.screen_height, bg='#d3fbfb')
        # 服务器Api
        label1 = tk.Label(self.frame1, text="服务器Api ", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"))
        entry1 = tk.Entry(self.frame1, bg='white', fg='grey')
        entry1.insert(0, "如: master, dev-xxx")
        entry1.bind("<FocusIn>", select_all_1)
        entry1.bind("<FocusOut>", check_entry_env)
        entry1.bind("<Leave>", check_entry_env)
        entry1.bind("<Return>", check_entry_env)
        label1.place(x=0.45*self.screen_width, y=0.01*self.screen_height, width=0.20*self.screen_width, height=0.09*self.screen_height)
        entry1.place(x=0.64*self.screen_width, y=0.01*self.screen_height, width=0.35*self.screen_width, height=0.09*self.screen_height)
        
        # 客户端版本
        label2 = tk.Label(self.frame1, text="客户端版本 ", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"))
        entry2 = tk.Entry(self.frame1, bg='white', fg='grey')
        entry2.insert(0, f"{st_config_change.CLIENT_VERSION_OLD}(当前默认)")
        entry2.bind("<FocusIn>", select_all_2)
        entry2.bind("<FocusOut>", check_config_version)
        entry2.bind("<Leave>", check_config_version)
        entry2.bind("<Return>", check_config_version)
        label2.place(x=0.45*self.screen_width, y=0.11*self.screen_height, width=0.20*self.screen_width, height=0.09*self.screen_height)
        entry2.place(x=0.64*self.screen_width, y=0.11*self.screen_height, width=0.35*self.screen_width, height=0.09*self.screen_height)

        # 游戏类型
        label3 = tk.Label(self.frame1, text="游戏类型 ", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"))
        label3.place(x=0.02*self.screen_width, y=0.05*self.screen_height, width=0.15*self.screen_width, height=0.1*self.screen_height)
        # 按钮选择
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var1_old = tk.IntVar()
        self.var2_old = tk.IntVar()
        self.var3_old = tk.IntVar()
        self.check1 = tk.Checkbutton(self.frame1, text="Test_channel_a", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"), variable=self.var1, command=lambda: on_check())
        self.check1.place(x=0.15*self.screen_width, y=0.00*self.screen_height, width=0.25*self.screen_width, height=0.06*self.screen_height)
        self.check2 = tk.Checkbutton(self.frame1, text="Test_channel_b", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"), variable=self.var2, command=lambda: on_check())
        self.check2.place(x=0.15*self.screen_width, y=0.07*self.screen_height, width=0.25*self.screen_width, height=0.06*self.screen_height)
        self.check3 = tk.Checkbutton(self.frame1, text="Test_channel_c", bg='#d3fbfb', font=(Font_title_type, Font_title_size, "bold"), variable=self.var3, command=lambda: on_check())
        self.check3.place(x=0.15*self.screen_width, y=0.14*self.screen_height, width=0.25*self.screen_width, height=0.06*self.screen_height)


        """2.设置工具的功能模块"""
        # 选择功能
        self.frame2 = Frame(self.screen, height=0.8*self.screen_height, bg='white')
        self.frame2.place()
        self.frame2_width = float(self.frame2.winfo_width()) * self.screen_width
        self.frame2_height = float(self.frame2.winfo_height()) * self.screen_height
        self.frame1.pack(side="top", fill="both", expand=True)
        self.frame2.pack(side="top", fill="both", expand=True)
        self.add_funcs()

    # 功能统一执行方法
    def test_func(self, func_str, *args):
        # 1.整理uid列表
        if self.test_uid_list_1 or self.test_uid_list_2:
            self.test_uid_list = self.test_uid_list_1 + self.test_uid_list_2
        else:
            pass
        if self.test_uid_list == []:
            messagebox.showinfo("提示", "Uid不能为空")
            return
        else:
            pass
        # 2.判断方法能否继续执行下去
        if self.need_init == False:
            return
        elif self.test_env_str == "master":
            if len(self.test_uid_list) > 10:
                messagebox.showinfo("提示", "master环境中, 单次执行Uid数不能超过10个")
                return
        else:
            pass
        # print(f"检查此处的self.test_uid_list: {self.test_uid_list}")

        if self.var1.get():
            game_type = "Test_channel_a"
        elif self.var2.get():
            game_type = "Test_channel_b"
        elif self.var3.get():
            game_type = "Test_channel_c"
        else:
            game_type = ""
        print(f"*****  游戏类型为: {game_type}, 测试环境为: {self.test_env_str}, 测试Uid账号列表为: {self.test_uid_list}, 调用函数方法为: {func_str}  *****")
        # res: set(), 记录执行中的信息并汇总显示
        res = call_fun_by_str(func_str, self.test_env_str, self.test_uid_list, *args)
        if not res:
            messagebox.showinfo("执行结果", "执行成功")
        else:
            messagebox.showinfo("执行结果", f"{str(res)}")
        # 关闭子窗口
        if self.kid_screen:
            self.kid_screen.destroy()


    # 功能撰写
    def add_funcs(self):
        """Type1"""
        label1 = tk.Label(self.screen, text="Type1: ", bg='white', font=(Font_title_type, Font_title_size, "bold"))
        x, y, width, height = self.frame2_width*0, self.frame2_height*0.24, self.frame2_width*0.1,self.frame2_height*0.1
        label1.place(x=x, y=y, width=width, height=height)
        #  1.test_func_1_1
        self.button_debug_1 = Button_test(self.screen, text='test_func_1_1', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_single_param_verify('test_func_1_1', self.screen, 'test_func_1_1'))
        args_list = self.get_button_index(1, 1)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_debug_1.place(x=x, y=y, width=width, height=height)

        #  2.test_func_1_2
        self.button_debug_2 = Button_test(self.screen, text='test_func_1_2', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_multi_param_verify('test_func_1_2', self.screen, 'test_func_1_2'))
        args_list = self.get_button_index(1, 2)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_debug_2.place(x=x, y=y, width=width, height=height)

        #  3.test_func_1_3
        self.button_debug_3 = Button_test(self.screen, text='test_func_1_3', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_single_param_verify('test_func_1_3', self.screen, 'test_func_1_3'))
        args_list = self.get_button_index(1, 3)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_debug_3.place(x=x, y=y, width=width, height=height)

        #  4.test_func_1_4
        self.button_debug_4 = Button_test(self.screen, text='test_func_1_4', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_multi_param_verify('test_func_1_4', self.screen, 'test_func_1_4'))
        args_list = self.get_button_index(1, 4)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_debug_4.place(x=x, y=y, width=width, height=height)

        """Type2"""
        label2 = tk.Label(self.screen, text="Type2: ", bg='white', font=(Font_title_type, Font_title_size, "bold"))
        x, y, width, height = self.frame2_width*0, self.frame2_height*0.37, self.frame2_width*0.1,self.frame2_height*0.1
        label2.place(x=x, y=y, width=width, height=height)
        #  1.test_func_2_1
        self.button_alliance_1 = Button_test(self.screen, text='test_func_2_1', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_single_param_verify('test_func_2_1', self.screen, 'test_func_2_1'))
        args_list = self.get_button_index(2, 1)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_alliance_1.place(x=x, y=y, width=width, height=height)
        
        #  2.test_func_2_2
        self.button_alliance_2 = Button_test(self.screen, text='test_func_2_2', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_multi_param_verify('test_func_2_2', self.screen, 'test_func_2_2'))
        args_list = self.get_button_index(2, 2)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_alliance_2.place(x=x, y=y, width=width, height=height)

        #  3.test_func_2_3
        self.button_alliance_3 = Button_test(self.screen, text='test_func_2_3', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_single_param_verify('test_func_2_3', self.screen, 'test_func_2_3'))
        args_list = self.get_button_index(2, 3)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_alliance_3.place(x=x, y=y, width=width, height=height)

        """Type3"""
        label3 = tk.Label(self.screen, text="Type3: ", bg='white', font=(Font_title_type, Font_title_size, "bold"))
        x, y, width, height = self.frame2_width*0, self.frame2_height*0.50, self.frame2_width*0.1,self.frame2_height*0.1
        label3.place(x=x, y=y, width=width, height=height)
        #  1.test_func_3_1
        self.button_rally_1 = Button_test(self.screen, text='test_func_3_1', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_multi_param_verify('test_func_3_1', self.screen, 'test_func_3_1'))
        args_list = self.get_button_index(3, 1)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_rally_1.place(x=x, y=y, width=width, height=height)

        #  2.test_func_3_2
        self.button_rally_2 = Button_test(self.screen, text='test_func_3_2', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_single_param_verify('test_func_3_2', self.screen, 'test_func_3_2'))
        args_list = self.get_button_index(3, 2)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_rally_2.place(x=x, y=y, width=width, height=height)

        """Type4"""
        label4 = tk.Label(self.screen, text="Type4: ", bg='white', font=(Font_title_type, Font_title_size, "bold"))
        x, y, width, height = self.frame2_width*0, self.frame2_height*0.63, self.frame2_width*0.1,self.frame2_height*0.1
        label4.place(x=x, y=y, width=width, height=height)
        #  1.test_func_4_1
        self.button_battlefield_1 = Button_test(self.screen, text='test_func_4_1', font=(Font_entry_type, Font_entry_size), fg='white', bg=Bg_Color_1, relief=RAISED, command=lambda: self.input_func_multi_param_verify('test_func_4_1', self.screen, 'test_func_4_1'))
        args_list = self.get_button_index(4, 1)
        x, y, width, height = self.frame2_width*args_list[0], self.frame2_height*args_list[1], self.frame2_width*args_list[2],self.frame2_height*args_list[3]
        self.button_battlefield_1.place(x=x, y=y, width=width, height=height)
       



    # 测试工具横纵坐标
    def get_button_index(self, row, column):
        row_step, column_step = 0.19, 0.13
        return [0.10+row_step*(column-1), 0.24+column_step*(row-1), 0.16, 0.1]

    # 双参数验证
    def input_func_multi_param_verify(self, func_str, screen, title):
        # 调用函数的参数不同, 作区分设计
        if func_str in ["test_func_1_2", "test_func_2_2", "test_func_4_1"]:
            title_text_1 = "param_a"
            title_text_2 = "param_b"
            info_text_1 = "请输入参数a"
            info_text_2 = "请输入参数b"
            info_text_3 = "参数a格式: xxx, 参数b格式: yyy"
        elif func_str in ["test_func_1_4", "test_func_2_2", "test_func_3_1"]:
            title_text_1 = "param_c"
            title_text_2 = "param_d"
            info_text_1 = "请输入参数c"
            info_text_2 = "请输入参数d"
            info_text_3 = "参数c格式: xxx, 参数d格式: yyy"
        else:
            title_text_1 = ""
            title_text_2 = ""
            info_text_1 = ""
            info_text_2 = ""
            info_text_3 = ""
        def select_all_1(event):
            entry1.select_range(0, "end")
        def select_all_2(event):
            entry2.select_range(0, "end")
        # 参数判断
        def check_entry_parama_1(event):
            if entry1.get().isdigit():
                self.test_uid_list_1 = get_entry_parama_1(entry1.get())
                if self.test_uid_list_1 == []:
                    entry1.delete(0, "end")
                    entry1.insert(0, info_text_1)
                    entry1.config(fg="grey")
                else:
                    entry1.config(fg="black")
            else:
                self.test_uid_list_1 = []
                entry1.delete(0, "end")
                entry1.insert(0, info_text_1)
                entry1.config(fg="grey") 
        def check_entry_parama_2(event):
            if "-" in entry2.get() or entry2.get().isdigit() or "," in entry2.get():
                self.test_uid_list_2 = get_entry_parama_2(entry2.get())
                if self.test_uid_list_2 == []:
                    entry2.delete(0, "end")
                    entry2.insert(0, info_text_2)
                    entry2.config(fg="grey")
                else:
                    entry2.config(fg="black")
            else:
                self.test_uid_list_2 = []
                entry2.delete(0, "end")
                entry2.insert(0, info_text_2)
                entry2.config(fg="grey") 
        # 判断测试环境是否为空
        if self.test_env_str == "":
            messagebox.showinfo("执行结果", "测试环境不能为空")
            return
        # 判断游戏类型是否选择
        if self.package_is_choosed == False:
            messagebox.showinfo("执行结果", "未选择游戏类型")
            return
        # 输入 Uid 和 Uid 的弹窗
        self.kid_screen, screen_width, screen_height = set_kid_screen(screen=screen, title=title)
        self.test_uid_list_1, self.test_uid_list_2 = [], []
        # 参数a
        label1 = tk.Label(self.kid_screen, text=title_text_1, bg='white', font=(Font_title_type, Font_title_size, "bold"))
        entry1 = tk.Entry(self.kid_screen, bg='white', fg='grey', highlightbackground="black")
        entry1.insert(0, info_text_1)
        entry1.bind("<FocusIn>", select_all_1)
        entry1.bind("<FocusOut>", check_entry_parama_1)
        entry1.bind("<Leave>", check_entry_parama_1)
        entry1.bind("<Return>", check_entry_parama_1)
        label1.place(x=0.30*screen_width, y=0.05*screen_height, width=0.40*screen_width, height=0.10*screen_height)
        entry1.place(x=0.20*screen_width, y=0.15*screen_height, width=0.60*screen_width, height=0.15*screen_height)
        # 参数b
        label2 = tk.Label(self.kid_screen, text=title_text_2, bg='white', font=(Font_title_type, Font_title_size, "bold"))
        entry2 = tk.Entry(self.kid_screen, bg='white', fg='grey', highlightbackground="black")
        entry2.insert(0, info_text_2)
        entry2.bind("<FocusIn>", select_all_2)
        entry2.bind("<FocusOut>", check_entry_parama_2)
        entry2.bind("<Leave>", check_entry_parama_2)
        entry2.bind("<Return>", check_entry_parama_2)
        label2.place(x=0.30*screen_width, y=0.35*screen_height, width=0.40*screen_width, height=0.10*screen_height)
        entry2.place(x=0.20*screen_width, y=0.45*screen_height, width=0.60*screen_width, height=0.15*screen_height)
        # 提示
        label3 = tk.Label(self.kid_screen, text=info_text_3, bg='white', font=(Font_info_type, Font_info_size), foreground="grey")
        label3.place(x=0.10*screen_width, y=0.62*screen_height, width=0.80*screen_width, height=0.15*screen_height)
        # 确认按钮
        button_confirm = Button_test(self.kid_screen, text='确认', font=(Font_entry_type, Font_entry_size), fg='white', bg='#0081ff', relief=RAISED, command=lambda: self.test_func(func_str))
        button_confirm.place(x=0.40*screen_width, y=0.82*screen_height, width=0.20*screen_width, height=0.15*screen_height)

    # 单参数验证
    def input_func_single_param_verify(self, func_str, screen, title):
        def select_all(event):
            entry1.select_range(0, "end")
        def check_entry_parama(event):
            # 初始化状态判断
            self.need_init = True
            if entry1.get().isdigit() or "," in entry1.get() or "-" in entry1.get():
                self.test_uid_list = get_entry_uid_list(entry1.get())
                if self.test_uid_list == []:
                    entry1.delete(0, "end")
                    entry1.insert(0, "请输入Uid")
                    entry1.config(fg="grey")
                # 特殊处理
                elif len(self.test_uid_list) > 5 and self.test_env_str == "master" and func_str == "xxx":
                    self.need_init = False
                    messagebox.showinfo("执行结果", "master环境中, 单次执行\"xxx\"方法的Uid数不超过5个")
                    return
                else:
                    entry1.config(fg="black")
            else:
                self.test_uid_list = []
                entry1.delete(0, "end")
                entry1.insert(0, "请输入Uid")
                entry1.config(fg="grey")

        # 判断测试环境是否为空
        if self.test_env_str == "":
            messagebox.showinfo("执行结果", "测试环境不能为空")
            return
        # 判断游戏类型是否选择
        if self.package_is_choosed == False:
            messagebox.showinfo("执行结果", "未选择游戏类型")
            return
        # 输入 Uid 和 Uid 的弹窗
        self.kid_screen, screen_width, screen_height = set_kid_screen(screen=screen, title=title)
        self.test_uid_list = []
        # 测试Uid
        label1 = tk.Label(self.kid_screen, text=f"Uid", bg='white', font=(Font_title_type, Font_title_size, "bold"))
        entry1 = tk.Entry(self.kid_screen, bg='white', fg='grey', highlightbackground="black")
        entry1.insert(0, "请输入Uid")
        entry1.bind("<FocusIn>", select_all)
        entry1.bind("<FocusOut>", check_entry_parama)
        entry1.bind("<Leave>", check_entry_parama)
        entry1.bind("<Return>", check_entry_parama)
        label1.place(x=0.35*screen_width, y=0.15*screen_height, width=0.30*screen_width, height=0.10*screen_height)
        entry1.place(x=0.20*screen_width, y=0.30*screen_height, width=0.60*screen_width, height=0.15*screen_height)
        # 提示
        label2 = tk.Label(self.kid_screen, text="1. 单Uid: 50001\n2. Uid区间: 50001-50005\n3. Uid列表: 50001,50003,50005", bg='white', font=(Font_info_type, Font_info_size), foreground="grey", justify="left")
        label2.place(x=0.10*screen_width, y=0.50*screen_height, width=0.80*screen_width, height=0.20*screen_height)
        # 确认按钮
        button_confirm = Button_test(self.kid_screen, text='确认', font=(Font_entry_type, Font_entry_size), fg='white', bg='#0081ff', relief=RAISED, command=lambda: self.test_func(func_str))
        button_confirm.place(x=0.40*screen_width, y=0.75*screen_height, width=0.20*screen_width, height=0.15*screen_height)

if __name__ == "__main__":
    screen = Tk()
    show_screen = TestStoolsDemo(screen, 'ST测试工具-demo')
    show_screen.load_all_func()
    screen.mainloop()