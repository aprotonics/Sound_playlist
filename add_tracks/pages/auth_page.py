import time

from .base_page import BasePage
from .locators import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthPage, self).__init__(*args, **kwargs)
        
        self.cred1 = "aprotonics@yandex.ru"
        self.cred2 = "243)ag#v9cG%"

    def auth(self, original_window):
        original_window = original_window
        
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
        
        current_url = self.driver.current_url
        
        file = "logs/logs.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{current_url} \n")


        time.sleep(2)
        

        sign_in_button1 = self.driver.find_element(*sign_in_button1_selector)
        sign_in_button1.click()

        time.sleep(1)

        auth_form = self.driver.find_element(*auth_form_selector)
        layout_content = self.driver.find_element(*layout_content_selector)
        authLoginInputToggle = self.driver.find_element(*authLoginInputToggle_selector)
        authLoginInputToggle = self.driver.find_element(*authLoginInputToggle_selector)
        authLoginInputToggle_input = self.driver.find_element(*authLoginInputToggle_input_selector)
        authLoginInputToggle_loginField = self.driver.find_element(*authLoginInputToggle_loginField_selector)
        field_inputWrapper = self.driver.find_element(*field_inputWrapper_selector)
        textinput = self.driver.find_element(*textinput_selector)
        textinput_Control = self.driver.find_element(*textinput_Control_selector)
        textinput_Control.send_keys(self.cred1)



        sign_in_button1 = self.driver.find_element(*sign_in_button1_selector)
        sign_in_button1.click()


        time.sleep(1)


        textinput_Control = self.driver.find_element(*textinput_Control_selector)
        textinput_Control.send_keys(self.cred2)


        sign_in_button2 = self.driver.find_element(*sign_in_button2_selector)
        sign_in_button2.click()

        self.driver.switch_to.window(original_window)
