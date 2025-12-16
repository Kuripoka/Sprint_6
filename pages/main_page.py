from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from locators.common_locators import *
from selenium.common.exceptions import NoSuchElementException
import time


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)    

    def accept_cookies(self):
        try:
            if self.driver.find_element(*COOKIE_ACCEPT_BUTTON).is_displayed():
                self.driver.find_element(*COOKIE_ACCEPT_BUTTON).click()
        except NoSuchElementException:
            pass

    def scroll_to_faq_section(self):
        for i in range(20):
            try:
                last_question = self.driver.find_element(*FAQ8_BEYOND_MKAD_QUESTION)
                if last_question.is_displayed():
                    return last_question
            except NoSuchElementException:
                pass
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.2)
    
    def click_faq_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        visible = self.wait.until(EC.visibility_of_element_located(locator))
        visible.click()

    def get_faq_answer_text(self, answer_locator):
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text
    
    def click_order_button_header(self):
        self.driver.find_element(*ORDER_BUTTON_HEADER).click()

    def scroll_to_order_button_in_page(self):
        for i in range(20):
            try:
                order_button_in_page = self.driver.find_element(*ORDER_BUTTON_PAGE)
                if order_button_in_page.is_displayed():
                    return order_button_in_page
            except NoSuchElementException:
                pass
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.2)

    def click_order_button_in_page(self):
        self.driver.find_element(*ORDER_BUTTON_PAGE).click()

    def click_yandex_logo(self):
        self.driver.find_element(*YANDEX_LOGO).click()

    def click_scooter_logo(self):
        self.driver.find_element(*SCOOTER_LOGO).click()   