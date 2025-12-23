import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import urls

class TestSiteNavigation:
    @pytest.mark.parametrize("logo", ["scooter", "yandex"])
    def test_logo_navigation(self, driver, logo):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        if logo == "scooter":
            main_page.click_order_button_header()
            order_page = OrderPage(driver)
            order_page.click_scooter_logo()
            assert urls.SCOOTER_URL in main_page.get_current_url()

        elif logo == "yandex":
            main_page.click_yandex_logo()
            main_page.wait_number_of_windows_to_be(2)
            main_page.switch_to_window_by_index(1)
            main_page.wait_url_contains(urls.DZEN_URL)
            assert urls.DZEN_URL in main_page.get_current_url()