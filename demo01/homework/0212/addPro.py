import requests
from login import Login


class Pro():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        self.s = s
        self.host = host
        # Login(s=self.s).login()
        self.cookie = Login().login()

    def addPro(self,
               name="测试23123122",
               aliasname="122",
               started="2022-03-16",
               ended="2022-03-16",
               desc="123123",
               id=0):
        url = self.host + "/project/add"
        datas = {
            "name": name,
            "aliasname": aliasname,
            "started": started,
            "ended": ended,
            "desc": desc,
            "id": id
        }
        res = self.s.post(url=url, data=datas, cookies=self.cookie)
        print(res.text)


if __name__ == '__main__':
    pr = Pro()
    pr.addPro()
