import pytest
from demo01.api.projectManage.addproject import Opmsaddproject


@pytest.mark.parametrize("name,aliasname,started,ended,desc,id,code",
                         [("ces1", "123", "2022-03-16", "2022-03-17", "321", 0, 1),
                          ("", "123", "2022-03-16", "2022-03-17", "321", 0, 0),
                          ("ces1", "", "2022-03-16", "2022-03-17", "321", 0, 0),
                          ("ces1", "123", "2022-03-16", "2022-03-17", "", 0, 0), ])
def test_addProject_01(name, aliasname, started, ended, desc, id, code):
    Opmsaddproject().login_post(username="libai", password="opms123456")
    res = Opmsaddproject().addProject(name=name, aliasname=aliasname, started=started, ended=ended, desc=desc, id=id)
    re_code = res.json()['code']
    # 断言
    assert re_code == code
