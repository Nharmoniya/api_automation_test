import requests
from crm.api.login import CRMLOGIN
from crm.com.getHost import getHost


class CRMADDBUS():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = getHost()
        self.cookie = CRMLOGIN().loginPost().json()['data']['accessToken']

    def addBus(self, busOpDesc="测试上传图片", busOpName="测试名字", busOpSource="测试资源", fileUrls=["D:\TestTrain\crm\api\busOpp\123.png"], id="",
               linkMan="123123",
               mobile="18652480015"):
        url = self.host + "/gateway/crmbo/business/create"
        head = {"Content-Type": "application/json",
                "h-request-token": self.cookie}
        datas = {
            "id": id,
            "busOpDesc": busOpDesc,
            "busOpName": busOpName,
            "busOpSource": busOpSource,
            "fileUrls":fileUrls,
            "linkMan": linkMan,
            "mobile": mobile,
        }

        res = self.s.post(url=url, headers=head, json=datas,)
        print(res.text)
        print(fileUrls)
        return res


if __name__ == '__main__':
    crm = CRMADDBUS()
    print(crm.cookie)
    crm.addBus()
