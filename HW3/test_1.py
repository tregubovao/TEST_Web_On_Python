import yaml
import time
from testpage import OperationHelper
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_1(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])        # login: "John777", pass: "9890279920"
    time.sleep(1)
    testpage.enter_password(testdata['pass'])
    time.sleep(1)
    testpage.enter_button()
    time.sleep(3)
    testpage.contact_button()
    time.sleep(1)
    testpage.enter_your_name(testdata["name_in_contact_us"])
    time.sleep(1)
    testpage.enter_your_email(testdata["e-mail"])
    time.sleep(1)
    testpage.enter_your_message(testdata["message"])
    time.sleep(1)
    testpage.contact_us_button()
    time.sleep(1)
    assert testpage.alert_window() == testdata["alert_message"]
    
if __name__  == "__main__":
    pytest.main(['-v'])



