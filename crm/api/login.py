import requests
from crm.com.getHost import getHost
from crm.com.getHost import getUser
from crm.com.getHost import getPassword


class CRMLOGIN():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = getHost()
        self.account = getUser()
        self.password = getPassword()

    def loginPost(self, account="10000", password="12356789"):
        url = self.host + "/gateway/ems/v1/login/byAccount"
        head = {"Content-Type": "application/json"}
        datas = {"account": account,
                 "password": password}
        res = self.s.post(url=url, headers=head, json=datas)
        return res


if __name__ == '__main__':
    crm = CRMLOGIN()
    crm.loginPost()
