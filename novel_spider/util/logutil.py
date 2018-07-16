# -*- coding: utf-8 -*-
'''
Created on 2018年4月8日

@author: Loong
'''
import logging
from logging.handlers import RotatingFileHandler
from config import configs
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)-12s [%(filename)s,%(funcName)s,%(lineno)d]: %(message)s')
# create a filehandler
# handler = logging.FileHandler('\logs\send_report.log')
# handler.setLevel(logging.INFO)
# create alogging format
# handler.setFormatter(formatter)
# add thehandlers to the logger


def get_log_path():
    log_path = configs["log_path"]
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return log_path


log_path= get_log_path()+"/get_novels.log";
#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler(log_path, maxBytes=10*1024*1024,backupCount=15)
Rthandler.setFormatter(formatter)

logger.addHandler(Rthandler)
