from readConfig import getIni


def getHost():
    host = getIni(name="\conf\data.ini", section='HOST', option='host')
    return host


getHost()
