import os
import configparser

# 引入configparser大类
import yaml

cf = configparser.ConfigParser()


def getIni(name, section, option):
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + name
    cf.read(filepath)
    res = cf[section][option]
    return res

def getYaml(file):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+file
    f = open(path,"r")
    cf = f.read()
    res = yaml.load(cf,Loader=yaml.CLoader)
    return res