from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import *
from locators.common_locators import *
from locators.order_page_locators import *

class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

# Шаг 1: Данные клиента
    def fill_first_name(self, name: str):
        self.driver.find_element(*FIRST_NAME_INPUT).send_keys(name)
    
    def fill_last_name(self, surname: str):
        self.driver.find_element(*LAST_NAME_INPUT).send_keys(surname)

    def fill_address(self, address: str):
        self.driver.find_element(*ADDRESS_INPUT).send_keys(address)

    def select_metro_station(self, station_locator):
        self.driver.find_element(*METRO_DROPDOWN).click()
        station = self.wait.until(EC.visibility_of_element_located(station_locator))
        station.click()

    def fill_phone(self, phone: str):
        self.driver.find_element(*PHONE_INPUT).send_keys(phone)
    
    def click_next_button(self):
        self.driver.find_element(*NEXT_BUTTON).click()

# Шаг 2: Детали заказа
    def fill_date(self, date: str):
        self.driver.find_element(*DATE_INPUT).send_keys(date, Keys.ENTER)
    
    def select_duration(self, duration_locator):
        self.driver.find_element(*RENT_DURATION_DROPDOWN).click()
        duration = self.wait.until(EC.visibility_of_element_located(duration_locator))
        duration.click()
    
    def select_color(self, color_locator):
        self.driver.find_element(*color_locator).click()
    
    def fill_comment(self, comment):
        self.driver.find_element(*COMMENT_INPUT).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*ORDER_BUTTON).click()


# Модальное окно подтверждения заказа
    def click_confirm_order_button(self):
        self.driver.find_element(*CONFIRMATIONAL_MODAL_YES_BUTTON).click()

    def click_check_order_status_button(self):
        self.driver.find_element(*SUCCESS_MODAL_CHECK_STATUS).click()

# Возврат через лого Самоката

    def click_scooter_logo(self):
        self.driver.find_element(*SCOOTER_LOGO).click()    