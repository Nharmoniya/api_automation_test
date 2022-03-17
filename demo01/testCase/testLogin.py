from demo01.getParam import Opms


class TestLogin:
    def __init__(self, op=Opms(host="http://123.56.170.43:8888")):
        self.op = op

    # 用户名为空测试
    def login_1(self):
        res = self.op.login_post(username="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')
    #密码为空测试
    def login_2(self):
        res = self.op.login_post(password="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')
    #用户名错误测试
    def login_3(self):
        res = self.op.login_post(username="123")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')
    #密码错误测试
    def login_4(self):
        res = self.op.login_post(password="123")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

if __name__ == '__main__':
    tl = TestLogin()
    tl.login_1()
    tl.login_2()
    tl.login_3()
    tl.login_4()
