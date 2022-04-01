from crm.com.readConfig import getIni
from crm.com.readConfig import getYaml

def getHost():
    host = getIni(name="\conf\data.ini", section="HOST", option="host")
    return host


def getUser():
    userName = getIni(name="\conf\data.ini", section="ADMIN", option="username")
    return userName


def getPassword():
    passWord = getIni(name="\conf\data.ini", section="ADMIN", option="password")
    return passWord

def getYamldb():
    host = getYaml(file="\conf\db.yaml")
    return host

getYamldb()