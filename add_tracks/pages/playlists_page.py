import time


from .base_page import BasePage
from .locators import *


class PlaylistsPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(PlaylistsPage, self).__init__(*args, **kwargs)

    def go_to_tracks_page(self):
        tracks_button = self.driver.find_element(*tracks_button_selector)
        tracks_button.click()

        time.sleep(1)
