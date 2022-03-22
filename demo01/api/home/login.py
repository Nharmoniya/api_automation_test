import requests


class Opmslogin():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        # requests中有session可以保存cookie
        self.s = s
        self.host = host

    def login_get(self):
        url = self.host + "/login"
        res = requests.get(url)

    def login_post(self, username="libai", password="opms123456"):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url, headers=head, data=datas)
        return res
