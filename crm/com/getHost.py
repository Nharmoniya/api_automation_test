from crm.com.readConfig import getIni


def getHost():
    host = getIni(name="\conf\data.ini", section="HOST", option="host")
    return host


def getUser():
    userName = getIni(name="\conf\data.ini", section="ADMIN", option="username")
    return userName


def getPassword():
    passWord = getIni(name="\conf\data.ini", section="ADMIN", option="password")
    return passWord

getUser()