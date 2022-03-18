import requests
import re


class Opms():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        # requests中有session可以保存cookie
        self.s = s
        self.host = host

    def login_get(self):
        url = self.host + "/login"
        res = requests.get(url)
        print(res.text)

    def login_post(self, username="libai", password="opms123456"):
        url = self.host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": username,
                 "password": password}
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.text)
        return res

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

    def geteditProject(self, id):
        url = self.host + "/project/edit/" + id
        res = self.s.get(url=url)
        print(res.text)

    def editProject(self, id):
        url = self.host + "/project/edit/" + id
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {
            "name": "测试23123122",
            "aliasname": "122",
            "started": "2022-03-16",
            "ended": "2022-03-16",
            "desc": "123123",
            "produserid": "请选择产品负责人",
            "testuserid": "请选择测试负责人",
            "publuserid": "请选择产品发布人",
            "id": id
        }
        res = self.s.post(url=url, headers=head, data=datas)
        print(res.text)
    #上传文件接口
    def uploadFile(self):
        url = self.host + "/uploadmulti"
        file = {"uploadfile":(open("name.txt"))}
        res = self.s.post(url=url, files=file)


if __name__ == '__main__':
    host = "http://123.56.170.43:8888"
    op = Opms(host=host)
    op.addProject()
