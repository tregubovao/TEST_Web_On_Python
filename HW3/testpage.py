from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocator:
    LOCATOR_INPUT_USERNAME = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_ENTER_BUTTON = (By.XPATH, """//*[@id="login"]/div[3]/button/span""")
    LOCATOR_CONTACT_BUTTON = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_INPUT_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_INPUT_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_INPUT_YOUR_MESSAGE = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BUTTON = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocator.LOCATOR_INPUT_USERNAME)
        login_field[0].clear()
        login_field[0].send_keys(word)        

    def enter_password(self, word):
        pass_field = self.find_element(TestSearchLocator.LOCATOR_INPUT_PASSWORD)
        pass_field[0].clear()
        pass_field[0].send_keys(word)

    def enter_button(self):
        self.find_element(TestSearchLocator.LOCATOR_ENTER_BUTTON)[0].click()

    def contact_button(self):
        self.find_element(TestSearchLocator.LOCATOR_CONTACT_BUTTON)[0].click()

    def enter_your_name(self, name):
        your_name = self.find_element(TestSearchLocator.LOCATOR_INPUT_YOUR_NAME)        
        your_name[0].clear()
        your_name[0].send_keys(name)

    def enter_your_email(self, email):
        your_email = self.find_element(TestSearchLocator.LOCATOR_INPUT_YOUR_EMAIL)
        your_email[0].clear()
        your_email[0].send_keys(email)

    def enter_your_message(self, message):
        your_message = self.find_element(TestSearchLocator.LOCATOR_INPUT_YOUR_MESSAGE)
        your_message[0].clear()
        your_message[0].send_keys(message)

    def contact_us_button(self):
        self.find_element(TestSearchLocator.LOCATOR_CONTACT_US_BUTTON)[0].click()

    def alert_window(self):
        alert = self.driver.switch_to.alert
        return alert.text
