import requests


class Opms():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        # requests中有session可以保存cookie
        self.s = s
        self.host = host

    def login_get(self):
        url = self.host + "/login"
        res = requests.get(url)
        print(res.text)

    def login_post(self):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": "libai",
                 "password": "opms123456"}
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.text)

    def proSer_1(self):
        url = self.host + "/project/manage"
        datas = "status=1&keywords=测试项目"
        para_url = url + "?" + datas
        res = self.s.get(para_url)
        print(res.text)

    def proSer_2(self):
        url = self.host + "/project/manage"
        data = {"status": "1",
                "keywords": "测试项目"}
        res = self.s.get(url=url, params=data)
        print(res.text)

    def addProject(self):
        url = self.host + "/project/add"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {
                 "name": "测试23123122",
                 "aliasname": "122",
                 "started": "2022-03-16",
                 "ended": "2022-03-16",
                 "desc": "123123",
                 "id": 0
                }
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.text)


if __name__ == '__main__':
    host = "http://123.56.170.43:8888"
    op = Opms(host=host)
    op.login_post()
    op.addProject()
