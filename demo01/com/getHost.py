from readConfig import getIni


def getHost():
    host = getIni(name="\conf\data.ini", section='HOST', option='host')
    return host


def getUser():
    user = getIni(name="\conf\data.ini", section='HOST', option='username')
    return user


def getPwd():
    pwd = getIni(name="\conf\data.ini", section='HOST', option='password')
    return pwd

