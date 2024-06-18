import time

from .base_page import BasePage
from .locators import *


class MainPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(MainPage, self).__init__(*args, **kwargs)

    def close_promo(self):
        close_button = self.driver.find_element(*close_button_selector)
        close_button.click()

    def go_to_auth_page(self):
        self.original_window = self.driver.current_window_handle
        
        auth_button = self.driver.find_element(*auth_button_selector)
        auth_button.click()

    def go_to_playlists_page(self):
        playlists_button = self.driver.find_element(*playlists_button_selector)
        playlists_button.click()

        time.sleep(1)
