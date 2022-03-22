import pytest
from demo01.api.projectManage.addproject import Opmsaddproject


@pytest.mark.parametrize()
def test_addProject_01(name, aliasname, started, ended, desc, id, code):
    Opmsaddproject().login_post(username="libai", password="opms123456")
    res = Opmsaddproject().addProject(name="ceshi", aliasname="123", started="2022-03-16", ended="2022-03-17", desc="123", id=0)
    res.json()['id']
    print(id)
