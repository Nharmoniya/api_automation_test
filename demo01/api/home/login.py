import requests
from demo01.com import readConfig
from demo01.com.getHost import getHost

class Opmslogin():
    def __init__(self, s=requests.session()):
        # requests中有session可以保存cookie
        self.s = s
        self.host = getHost()

    def login_get(self):
        url = self.host + "/login"
        res = requests.get(url)

    def login_post(self, username="libai", password="opms123456"):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.status_code)
        return res


if __name__ == '__main__':
    host = "http://123.56.170.43:8888"
    head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    datas = {"username": "libai",
             "password": "opms123456"}
    name = readConfig.getTxt("\conf\data.txt")[0]
    lg = Opmslogin().login_post(username=name)
