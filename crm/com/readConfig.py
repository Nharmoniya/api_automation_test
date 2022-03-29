import os
import configparser

# 引入configparser大类
cf = configparser.ConfigParser()


def getIni(name, section, option):
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + name
    cf.read(filepath)
    res = cf[section][option]
    return res
