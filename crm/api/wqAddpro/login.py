import requests


class WQLOGIN():
    def __init__(self, s=requests.session(), host="http://test.wqjgj.com"):
        self.s = s
        self.host = host

    def loginPost(self):
        url = self.host + "/member/login.php"
        datas = {"forward": "http://test.wqjgj.com/",
                 "auth": "",
                 "fei": "",
                 "username": "ceshi22",
                 "password": "12356789",
                 "submit": "登录", }
        res = self.s.post(url=url, data=datas)
        print(res.text)


if __name__ == '__main__':
    wq = WQLOGIN()
    wq.loginPost()
