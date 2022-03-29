import pytest
from crm.api.login import CRMLOGIN

# 笛卡尔积
@pytest.mark.parametrize("account", ["", "10000", "l10000"])
@pytest.mark.parametrize("password", ["", "12356789", "123456"])
def test_login_01(account, password):
    res = CRMLOGIN().loginPost(account=account, password=password)
    code = res.status_code
    assert code == 200

