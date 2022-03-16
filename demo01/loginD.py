import requests


# 将登录变为函数
class Login():

    def erpLogin(self):
        host = "http://123.56.170.43:3000/jshERP-boot"
        login_url = host + "/user/login"
        head = {"Conetent-Type": "application/json;charset=UTF-8"}
        datas = {"loginName": "root",
                 "password": "6c07ae8849fdcef7621d816d56c44db5"
                 }
        res = requests.post(url=login_url, headers=head, json=datas)
        print(res.text)

    def opmsLogin(self):
        host = "http://123.56.170.43:8888"
        url = host + "/login"
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
        datas = {"username": "libai",
                 "password": "opms123456"}
        res = requests.post(url=url, headers=head, data=datas)
        print(res.text)

#定义一个opmslog类
class opmsLog():
    def __init__(self, host="http://123.56.170.43:8888"):
        self.host = host
#init初始函数必执行一次
    def login(self, head, datas):
        url = self.host + '/login'
        res = requests.post(url=url, headers=head, data=datas)
        print(res.text)

    def logout(self):
        url = self.host + '/logout'
        res = requests.get(url=url)
        print(res.text)

#定义一个ERPlog类
class erpLog():
    def __init__(self,host="http://123.56.170.43:3000"):
       self.host=host
    def login(self,head,datas):
        url=self.host+'/user/login'
        res=requests.post(url=url,headers=head,data=datas)
        print(res.text)

    def logout(self):
        url=self.host+'/user/logout'
        res=requests.get(url=url)
        print(res.text)


#main主函数
if __name__ == '__main__':
    head = {"Content-Type": "application/json;charset=UTF-8"}
    datas = {"username": "root",
             "password": "csyz.1234"}
    #实例化opmslog类
    erp=erpLog()
    erp.login(head,datas)
