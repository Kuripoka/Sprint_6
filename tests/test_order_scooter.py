import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import SUCCESS_MODAL_WINDOW
from data import CLIENT_DATA_1, CLIENT_DATA_2

CLIENT_DATASETS = [
    (CLIENT_DATA_1, 1),
    (CLIENT_DATA_2, 2),
]

class TestOrderScooter:
    @pytest.mark.parametrize("client_data, dataset_number", CLIENT_DATASETS)
    def test_order_creation(self, driver, client_data, dataset_number):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        if dataset_number > 1:
            main_page.click_order_button_in_page()
        else:
            main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.fill_first_name(client_data["first_name"])
        order_page.fill_last_name(client_data["last_name"])
        order_page.fill_address(client_data["address"])
        order_page.fill_phone(client_data["phone"])
        order_page.select_metro_station(client_data["metro_station"])
        order_page.click_next_button()
        order_page.fill_date(client_data["date"])
        order_page.select_duration(client_data["duration"])
        order_page.select_color(client_data["color"])
        order_page.fill_comment(client_data["comment"])
        order_page.click_order_button()
        order_page.click_confirm_order_button()
        assert "Заказ оформлен" in order_page.wait_and_find_element(SUCCESS_MODAL_WINDOW).text
        order_page.click_check_order_status_button()
        order_page.click_scooter_logo()