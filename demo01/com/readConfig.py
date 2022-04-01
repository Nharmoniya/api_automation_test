import os
import configparser
import yaml

# 引入configparser大类
cf = configparser.ConfigParser()


def getIni(name, section, option):
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + name
    cf.read(filepath)
    res = cf[section][option]
    print(res)
    return res


def getyaml(file):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + file
    f = open(path, "r")
    cf = f.read()
    res = yaml.load(cf, Loader=yaml.CLoader)
    return res
#
#
# # path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\conf\db.yaml"
#
# res = getyaml(file="\conf\db.yaml")
# print(res['host'][0][1])
# def getTxt(name="\conf\data.txt"):
#     # 1、先获取当前工程的绝对路径
#     # 2、工程绝对路径+文件相对路径
#     filepath = os.path.dirname(os.getcwd()) + name
#     with open(filepath, 'r') as f:
#         res = f.readlines()
#     return res
#
#
# names = getTxt()
# for i in names:
#     print("列表里的值是:"+i)
