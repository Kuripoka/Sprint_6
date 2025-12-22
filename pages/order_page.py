from selenium.webdriver.common.keys import Keys
from locators.common_locators import CommonLocators
from locators.order_page_locators import *
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

# Шаг 1: Данные клиента
    @allure.step("Заполнение имени клиента")
    def fill_first_name(self, name: str):
        self.wait_and_send_keys(FIRST_NAME_INPUT, name)
    
    @allure.step("Заполнение фамилии клиента")
    def fill_last_name(self, surname: str):
        self.wait_and_send_keys(LAST_NAME_INPUT, surname)

    @allure.step("Заполнение адреса клиента")
    def fill_address(self, address: str):
        self.wait_and_send_keys(ADDRESS_INPUT, address)

    @allure.step("Выбор станции метро")
    def select_metro_station(self, station_locator):
        self.wait_and_click(METRO_DROPDOWN)
        self.wait_and_click(station_locator)

    @allure.step("Заполнение номера телефона клиента")
    def fill_phone(self, phone: str):
        self.wait_and_send_keys(PHONE_INPUT, phone)
    
    @allure.step("Нажатие на кнопку Далее (переход на форму деталей заказа)")
    def click_next_button(self):
        self.wait_and_click(NEXT_BUTTON)

# Шаг 2: Детали заказа
    @allure.step("Заполнение даты заказа")
    def fill_date(self, date: str):
        element = self.wait_and_find_element(DATE_INPUT)
        element.send_keys(date, Keys.ENTER)

    @allure.step("Выбор длительности заказа")
    def select_duration(self, duration_locator):
        self.wait_and_click(RENT_DURATION_DROPDOWN)
        self.wait_and_click(duration_locator)
    
    @allure.step("Выбор цвета самоката")
    def select_color(self, color_locator):
        self.wait_and_click(color_locator)
    
    @allure.step("Заполнение комментария")
    def fill_comment(self, comment: str):
        self.wait_and_send_keys(COMMENT_INPUT, comment)

    @allure.step("Нажатие кнопки Заказать (отправка запроса заказа)")
    def click_order_button(self):
        self.wait_and_click(ORDER_BUTTON)


# Модальное окно подтверждения заказа
    @allure.step("Нажатие кнопки Да в модальном окне подтверждения заказа")
    def click_confirm_order_button(self):
        self.wait_and_click(CONFIRMATIONAL_MODAL_YES_BUTTON)

    @allure.step("Нажатие кнопки Посмотреть статус (после отправки запроса заказа)")
    def click_check_order_status_button(self):
        self.wait_and_click(SUCCESS_MODAL_CHECK_STATUS)

# Возврат через лого Самоката
    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self):
        self.wait_and_click(CommonLocators.SCOOTER_LOGO)    