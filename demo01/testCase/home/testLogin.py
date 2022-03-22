import pytest
from demo01.api.home.login import Opmslogin


# 测试登录接口,用户名为空
#参数化用户名和密码
@pytest.mark.parametrize("names,password,code", [("", "", 0),
                                                 ("libai", "opms123456", 1),
                                                 ("libai123", "opms", 0), ])
def test_login_1(names, code, password):
    res = Opmslogin().login_post(username=names, password=password)
    re_code = res.json()['code']
    # 断言
    assert re_code == code

