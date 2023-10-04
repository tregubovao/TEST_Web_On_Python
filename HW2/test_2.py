import yaml
import time
from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(testdata["login2"])

    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(testdata["passwd2"])
    
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(1)    

    btn_selector3 = """#create-btn"""
    btn_plus = site.find_element("css", btn_selector3)
    btn_plus.click()
    time.sleep(1)

    x_selector11 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""    
    input11 = site.find_element("xpath", x_selector11)
    input11.send_keys(testdata["title"])
    time.sleep(1)

    x_selector12 = """//*[@id="create-item"]/div/div/div[2]/div/label"""
    input12 = site.find_element("xpath", x_selector12)
    input12.send_keys(testdata["description"])
    time.sleep(1)

    x_selector13 = """//*[@id="create-item"]/div/div/div[3]/div/label"""
    input13 = site.find_element("xpath", x_selector13)
    input13.send_keys(testdata["content"])
    time.sleep(1)

    btn_selector13 = """#create-item > div > div > div:nth-child(7) > div > button > span"""
    btn_save = site.find_element("css", btn_selector13)
    btn_save.click()
    time.sleep(1)

    x_selector33 = """//*[@id="app"]/main/div/div[1]/h1"""
    title_of_post = site.find_element("xpath", x_selector33)
    assert title_of_post.text == testdata["title"]

if __name__  == "__main__":
    pytest.main(['-v'])
