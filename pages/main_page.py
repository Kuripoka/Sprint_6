from locators.main_page_locators import *
from locators.common_locators import CommonLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step("Принять cookies (если баннер присутствует на странице)")
    def accept_cookies(self):
        self.try_to_click(CommonLocators.COOKIE_ACCEPT_BUTTON)
    
    @allure.step("Клик по кнопке заказа в заголовке страницы")    
    def click_order_button_header(self):
        self.wait_and_click(ORDER_BUTTON_HEADER)
    
    @allure.step("Клик по кнопке заказа в теле страницы")
    def click_order_button_in_page(self):
        self.scroll_into_view(ORDER_BUTTON_PAGE)
        self.wait_and_click(ORDER_BUTTON_PAGE)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.wait_and_click(CommonLocators.YANDEX_LOGO)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.wait_and_click(CommonLocators.SCOOTER_LOGO)

    @allure.step("Клик по вопросу из FAQ: {question_locator}")
    def click_faq_question(self, question_locator):
        self.scroll_into_view(question_locator)
        self.wait_and_click(question_locator)

    @allure.step("Забор текста ответа из FAQ: {answer_locator}")
    def get_faq_answer(self, answer_locator):
        return self.wait_and_find_element(answer_locator).text