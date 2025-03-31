# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import logging
import time
import gevent
from gevent.pool import Pool
from gevent import monkey 
monkey.patch_all()


def concurrent_uid_requests(func, uid_list, pool_number, *args, **kwargs):
    # 定义最大并发数
    pool = Pool(pool_number)
    start_time = time.time()
    # 任务派发
    threads = [pool.spawn(func, uid, *args, **kwargs) for uid in uid_list]
    # 在此阻塞，等所有协程全部完成退出，这一步才执行完
    gevent.joinall(threads)
    end_time = time.time()
    logging.info("总耗时：{}".format(end_time-start_time))