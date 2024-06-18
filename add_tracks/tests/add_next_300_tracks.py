from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.playlists_page import PlaylistsPage
from pages.tracks_page import TracksPage


URL = "https://music.yandex.ru/"
URL2 = "https://music.yandex.ru/users/aprotonics/playlists"

class TestFastOrder():
    def test_fast_order(self, driver):
        main_page = MainPage(driver, URL)
        main_page.open()
        main_page.close_promo()
        main_page.go_to_auth_page()

        auth_page = AuthPage(driver, URL)
        auth_page.auth(main_page.original_window)

        main_page = MainPage(driver, URL)
        main_page.open()

        playlists_page = PlaylistsPage(driver, URL2)
        playlists_page.open()
        playlists_page.go_to_tracks_page()

        tracks_page = TracksPage(driver, URL)
        tracks_page.add_next_tracks(300)














