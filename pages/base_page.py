import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from data import Config
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)

    @allure.step("Скролл страницы до элемента")
    def scroll_into_view(self, locator):
        for i in range(20):
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                pass
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(0.2)

    @allure.step("Определение видимости элемента в текущий момент")
    def wait_and_find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Обязательный клик по элементу {locator}")
    def wait_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()
    
    @allure.step("Попытка клика по элементу {locator}, пропуск если элемент не найден")
    def try_to_click(self, locator):
        try:
            element = self.driver.find_element(*locator)
            element.click()
        except NoSuchElementException:
            pass

    @allure.step("Заполнение формы текстом")
    def wait_and_send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание содержания текста в URL")
    def wait_url_contains(self, text):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.url_matches(rf"^{text}.*"))

    @allure.step("Ожидание конкретного количества вкладок браузера")
    def wait_number_of_windows_to_be(self, count: int):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.number_of_windows_to_be(count))

    @allure.step("Переключение на конкретную вкладку браузера")
    def switch_to_window_by_index(self, index: int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Забор текущего состояния адресной строки")
    def get_current_url(self):
        return self.driver.current_url