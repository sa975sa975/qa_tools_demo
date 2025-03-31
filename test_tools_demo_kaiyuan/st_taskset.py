# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import time

class StTaskSet:
    def __init__(self):
        pass

    def init_task_set(self, uid: int):
        self.start_time = time.perf_counter()
        self.count: int = 0
        self.uid = uid

