import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import *
from locators.order_page_locators import *
from data import URL

@pytest.mark.parametrize("logo", ["scooter", "yandex"])
def test_logo_navigation(driver, logo):
    if logo == "scooter":
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.click_scooter_logo()
        assert URL in driver.current_url

    elif logo == "yandex":
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url