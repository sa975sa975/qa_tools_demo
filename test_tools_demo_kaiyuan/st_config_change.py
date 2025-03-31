# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# # master服务器、dev
CLIENT_VERSION = 'xx.xx.xx'
CLIENT_VERSION_OLD = CLIENT_VERSION

# 更新客户端版本号
def get_new_client_version(client_version):
    global CLIENT_VERSION, CLIENT_FULL_VERSION
    CLIENT_VERSION = str(client_version)
    CLIENT_FULL_VERSION = str(client_version) + str(client_version)

# 更新账号前缀
def get_new_project(project):
    global PROJECT
    PROJECT = str(project)