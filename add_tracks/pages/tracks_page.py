import time

from .base_page import BasePage
from .locators import *

from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class TracksPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(TracksPage, self).__init__(*args, **kwargs)

        self.track_titles = []
        self.track_next_titles = []
        self.tracks_titles_count = 0

    def get_track_title(self):
        for i in range(10):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        track_card = self.tracks_titles_list[1]

        d_track__start_column = track_card.find_element(*d_track__start_column_selector)
        track_title = track_card.find_element(*track_title_selector).get_attribute("title")
        self.track_titles.append(track_title)


        file = "track_titles.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            for value in self.track_titles:
                f.write(f"{value} \n")

    def get_tracks_titles(self):
        number_of_tracks_to_read = 20
        
        for i in range(number_of_tracks_to_read + 20):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(number_of_tracks_to_read + 20):
            ActionChains(self.driver).key_down(Keys.UP).perform()
        
        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_count = len(self.tracks_titles_list)

        file = "track_titles_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_count} \n")

        
        for i in range(number_of_tracks_to_read):
            track_card = self.tracks_titles_list[i]
            d_track__start_column = track_card.find_element(*d_track__start_column_selector)
            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            self.track_titles.append(track_title)

            ActionChains(self.driver).key_down(Keys.DOWN).perform()


        file = "tracks_titles.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            for value in self.track_titles:
                f.write(f"{value} \n")

    def count_tracks_titles(self):
        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(100):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_count = len(self.tracks_titles_list)

        file = "track_titles_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_count} \n")

    def add_track(self):
        track_card = self.tracks_titles_list[1]
        ActionChains(self.driver).move_to_element(track_card).perform()
        track_title = track_card.find_element(*track_title_selector).get_attribute("title")
        track_menu = track_card.find_element(*track_menu_selector)
        track_menu.click()

        track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
        track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
        track_menu_tab_item.click()

        track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
        track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
        track_menu_playlist_to_add.click()
    
    def add_tracks(self):
        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(100):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)
        
        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_count = len(self.tracks_titles_list)

        file = "logs/track_titles_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_count} \n")


        number_of_tracks_to_add = 100

        d_subhead__title_main = self.driver.find_element(*d_subhead__title_main_selector)
        d_subhead__title_main.click()

        for i in range(number_of_tracks_to_add):
            track_card = self.tracks_titles_list[i]

            ActionChains(self.driver).move_to_element(track_card).perform()

            time.sleep(0.2)

            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            track_menu = track_card.find_element(*track_menu_selector)
            track_menu.click()

            track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
            track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
            track_menu_tab_item.click()

            track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
            track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
            track_menu_playlist_to_add.click()

            self.track_titles.append(track_title)

            file = "logs/tracks_titles.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                for value in self.track_titles:
                    f.write(f"{value} \n")


            ActionChains(self.driver).key_down(Keys.DOWN).perform()

            time.sleep(0.3)
    

    def add_next_tracks(self, next_track_id):
        next_track_id = next_track_id
        
        self.track_next_titles = []
        last_track_id_in_session = next_track_id + 100

        time.sleep(1)

        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(last_track_id_in_session):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_next_count = len(self.tracks_titles_list)

        file = f"logs/track_titles_next_{next_track_id}_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_next_count} \n")


        number_of_tracks_to_add = 100

        track_card = self.tracks_titles_list[0]
        d_track__info = track_card.find_element(*d_track__info_selector)
        d_track__info.click()
        
        for i in range(number_of_tracks_to_add):
            track_card = self.tracks_titles_list[i]

            ActionChains(self.driver).move_to_element(track_card).perform()

            time.sleep(0.3)

            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            track_menu = track_card.find_element(*track_menu_selector)
            track_menu.click()

            track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
            track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
            track_menu_tab_item.click()

            track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
            track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
            track_menu_playlist_to_add.click()

            self.track_next_titles.append(track_title)

            file = f"logs/tracks_next_{next_track_id}_titles.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                for value in self.track_next_titles:
                    f.write(f"{value} \n")


            ActionChains(self.driver).key_down(Keys.DOWN).perform()

            time.sleep(0.4)

    def add_next_tracks_page(self, next_track_id):
        next_track_id = next_track_id
        
        self.track_next_titles = []
        last_track_id_in_session = next_track_id + 100
        next_track_on_page_id = next_track_id + 1250

        time.sleep(1)

        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(last_track_id_in_session):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_next_count = len(self.tracks_titles_list)

        file = f"logs/track_titles_next_{next_track_on_page_id}_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_next_count} \n")


        number_of_tracks_to_add = 100

        track_card = self.tracks_titles_list[0]
        d_track__info = track_card.find_element(*d_track__info_selector)
        d_track__info.click()
        
        for i in range(number_of_tracks_to_add):
            track_card = self.tracks_titles_list[i]

            ActionChains(self.driver).move_to_element(track_card).perform()

            time.sleep(0.3)

            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            track_menu = track_card.find_element(*track_menu_selector)
            track_menu.click()

            track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
            track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
            track_menu_tab_item.click()

            track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
            track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
            track_menu_playlist_to_add.click()

            self.track_next_titles.append(track_title)

            file = f"logs/tracks_next_{next_track_on_page_id}_titles.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                for value in self.track_next_titles:
                    f.write(f"{value} \n")


            ActionChains(self.driver).key_down(Keys.DOWN).perform()

            time.sleep(0.4)

    def add_next_tracks_second_page(self, next_track_id):
        next_track_id = next_track_id
        
        self.track_next_titles = []
        last_track_id_in_session = next_track_id + 100
        next_track_on_page_id = next_track_id + 2500

        time.sleep(1)

        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(last_track_id_in_session):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_next_count = len(self.tracks_titles_list)

        file = f"logs/track_titles_next_{next_track_on_page_id}_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_next_count} \n")


        number_of_tracks_to_add = 100

        track_card = self.tracks_titles_list[0]
        d_track__info = track_card.find_element(*d_track__info_selector)
        d_track__info.click()
        
        for i in range(number_of_tracks_to_add):
            track_card = self.tracks_titles_list[i]

            ActionChains(self.driver).move_to_element(track_card).perform()

            time.sleep(0.3)

            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            track_menu = track_card.find_element(*track_menu_selector)
            track_menu.click()

            track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
            track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
            track_menu_tab_item.click()

            track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
            track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
            track_menu_playlist_to_add.click()

            self.track_next_titles.append(track_title)

            file = f"logs/tracks_next_{next_track_on_page_id}_titles.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                for value in self.track_next_titles:
                    f.write(f"{value} \n")


            ActionChains(self.driver).key_down(Keys.DOWN).perform()

            time.sleep(0.4)

    def add_next_tracks_third_page(self, next_track_id):
        next_track_id = next_track_id
        
        self.track_next_titles = []
        last_track_id_in_session = next_track_id + 100
        next_track_on_page_id = next_track_id + 3750

        time.sleep(1)

        for i in range(5):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
        
        for i in range(last_track_id_in_session):
            ActionChains(self.driver).key_down(Keys.DOWN).perform()

        time.sleep(1)

        self.tracks_titles_list = self.driver.find_elements(*tracks_titles_selector)
        self.tracks_titles_next_count = len(self.tracks_titles_list)

        file = f"logs/track_titles_next_{next_track_on_page_id}_count.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(f"{self.tracks_titles_next_count} \n")


        number_of_tracks_to_add = 100

        track_card = self.tracks_titles_list[0]
        d_track__info = track_card.find_element(*d_track__info_selector)
        d_track__info.click()
        
        for i in range(number_of_tracks_to_add):
            track_card = self.tracks_titles_list[i]

            ActionChains(self.driver).move_to_element(track_card).perform()

            time.sleep(0.3)

            track_title = track_card.find_element(*track_title_selector).get_attribute("title")
            track_menu = track_card.find_element(*track_menu_selector)
            track_menu.click()

            track_menu_tab = self.driver.find_element(*track_menu_tab_selector)
            track_menu_tab_item = track_menu_tab.find_element(*track_menu_tab_item_selector)
            track_menu_tab_item.click()

            track_menu_tab2 = self.driver.find_element(*track_menu_tab2_selector)
            track_menu_playlist_to_add = track_menu_tab2.find_element(*track_menu_playlist_to_add_selector)
            track_menu_playlist_to_add.click()

            self.track_next_titles.append(track_title)

            file = f"logs/tracks_next_{next_track_on_page_id}_titles.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                for value in self.track_next_titles:
                    f.write(f"{value} \n")


            ActionChains(self.driver).key_down(Keys.DOWN).perform()

            time.sleep(0.4)



















