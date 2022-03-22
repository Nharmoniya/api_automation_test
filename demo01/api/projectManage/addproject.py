import requests


class Opmsaddproject():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        # requests中有session可以保存cookie
        self.s = s
        self.host = host

    def login_post(self, username="libai", password="opms123456"):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url, headers=head, data=datas)
        return res

    def addProject(self,
                   name="测试23123122",
                   aliasname="122",
                   started="2022-03-16",
                   ended="2022-03-16",
                   desc="123123",
                   id=0):
        url = self.host + "/project/add"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {
            "name": name,
            "aliasname": aliasname,
            "started": started,
            "ended": ended,
            "desc": desc,
            "id": id
        }
        res = self.s.post(url=url, headers=head, data=datas)
        # 将json中的id提取出来
        # print(res.text )
        # return res.json()["id"]
        # 用正则将id提取出来
        # id = re.findall(r'"id":"(.*?)"', res.text)
        # 发现时列表后通过索引下标提取
        print(res.text)
        return res
