# from selenium.webdriver.common.by import By 
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']     

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator), 
                                                      message="Элемент не найден")
    
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)
    
    def close(self):
        self.driver.close()




