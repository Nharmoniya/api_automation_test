import pytest
from demo01.api.home.login import Opms


# 测试登录接口,用户名为空
def test_login_1():
    res = Opms().login_post(username="")
    code = res.json()['code']
    # 断言
    assert code == 0

# 测试登录接口,密码为空
def test_login_2():
    res = Opms().login_post(password="")
    code = res.json()['code']
    # 断言
    assert code == 0
