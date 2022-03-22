from demo01.others.getParam import Opms


class TestLogin:
    def __init__(self, op=Opms(host="http://123.56.170.43:8888")):
        self.op = op

    def test_login_0(self):
        res = self.op.login_post(username="libai", password="opms123456")
        message = res.json()['message']
        print(message)

    # 用户名为空测试
    def login_1(self):
        res = self.op.login_post(username="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 密码为空测试
    def test_login_2(self):
        res = self.op.login_post(password="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 用户名错误测试
    def login_3(self):
        res = self.op.login_post(username="123")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 密码错误测试
    def login_4(self):
        res = self.op.login_post(password="123")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 添加项目
    def addpro_0(self):
        res = self.op.addProject(name="测试傻逼")
        message = res.json()['message']
        print(message)

    # 项目名为空测试
    def addpro_1(self):
        res = self.op.addProject(name="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 别名为空测试
    def addpro_2(self):
        res = self.op.addProject(aliasname="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')

    # 描述为空测试
    def addpro_3(self):
        res = self.op.addProject(desc="")
        code = res.json()['code']
        if code == 0:
            print('测试通过')
        else:
            print('测试失败')


if __name__ == '__main__':
    tl = TestLogin()
    tl.test_login_0()
    tl.addpro_0()
    tl.addpro_1()
    tl.addpro_2()
    tl.addpro_3()
