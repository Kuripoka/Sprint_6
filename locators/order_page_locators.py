from selenium.webdriver.common.by import By

# Шаг 1: Данные клиента
FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
METRO_STATION_CHRKZ = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Черкизовская']/ancestor::button[1]")
METRO_STATION_PREOBR_SQR = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Преображенская площадь']/ancestor::button[1]")
PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

# Шаг 2: Детали заказа
DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
RENT_DURATION_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
RENT_DURATION_ONE_DAY = (By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space()='сутки']")
RENT_DURATION_TWO_DAYS = (By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space()='двое суток']")
COLOR_CHECKBOX_BLACK = (By.ID, "black")
COLOR_CHECKBOX_GREY = (By.ID, "grey")
COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")

# Модальное окно заказа
CONFIRMATIONAL_MODAL_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
SUCCESS_MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal') and contains(., 'Заказ оформлен')]")
SUCCESS_MODAL_CHECK_STATUS = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA > button:nth-child(1)")