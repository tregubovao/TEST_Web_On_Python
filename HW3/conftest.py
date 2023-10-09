import pytest, time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


@pytest.fixture(scope="session")
def browser():    
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)        
    driver.maximize_window()
    yield driver
    driver.quit()


    
        

