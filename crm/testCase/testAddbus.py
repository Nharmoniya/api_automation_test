import pytest
from crm.api.busOpp.addBus import CRMADDBUS


# 笛卡尔积
@pytest.mark.parametrize("id", [""])
@pytest.mark.parametrize("busOpDesc", ["", "测试不为空", "测试中文", "ceshiyingwen", "yingwen+123", "123", ";;;;"])
@pytest.mark.parametrize("busOpName", ["", "测试不为空", "测试中文", "ceshiyingwen", "yingwen+123", "123", ";;;;"])
@pytest.mark.parametrize("busOpSource", ["21"])
@pytest.mark.parametrize("fileUrls", [])
@pytest.mark.parametrize("linkMan", ["", "测试不为空", "测试中文", "ceshiyingwen", "yingwen+123", "123", ";;;;"])
@pytest.mark.parametrize("mobile", ["18652480015"])
def test_login_01(id, busOpDesc, busOpName, busOpSource, fileUrls, linkMan, mobile):
    res = CRMADDBUS().addBus(id=id, busOpDesc=busOpDesc, busOpName=busOpName, busOpSource=busOpSource,
                             fileUrls=fileUrls, linkMan=linkMan, mobile=mobile)
    code = res.status_code
    assert code == 200

#必填测试
@pytest.mark.parametrize("id, busOpDesc, busOpName, busOpSource, fileUrls, linkMan, mobile,code",
                         [("", "测试1", "测试2", "21", [], "测试人", "18652480015", 0),
                          ("", "", "测试2", "21", [], "测试人", "18652480015", 0),
                          ("", "", "", "21", [], "测试人", "18652480015", 0),
                          ("", "", "", "", [], "测试人", "18652480015", 0),
                          ("", "", "", "", [], "", "18652480015", 0),
                          ("", "", "", "", [], "", "", 0)])
def test_login_02(id, busOpDesc, busOpName, busOpSource, fileUrls, linkMan, mobile, code):
    res = CRMADDBUS().addBus(id=id, busOpDesc=busOpDesc, busOpName=busOpName, busOpSource=busOpSource,
                             fileUrls=fileUrls, linkMan=linkMan, mobile=mobile)
    reCode = res.json()['code']
    assert reCode == code
