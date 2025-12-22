from locators.order_page_locators import METRO_STATION_CHRKZ, METRO_STATION_PREOBR_SQR, COLOR_CHECKBOX_BLACK, COLOR_CHECKBOX_GREY, RENT_DURATION_ONE_DAY, RENT_DURATION_TWO_DAYS

class urls:
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "https://dzen.ru/"

class Config: 
    DEFAULT_TIMEOUT = 10

FAQ_ANSWERS = {
    1: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    2: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
    3: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
    4: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
    5: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    6: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
    7: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
    8: "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
}

CLIENT_DATA_1 = {
    "first_name": "Иван",
    "last_name": "Иванов",
    "address": "Москва, ул. Черкизовская, 1",
    "metro_station": METRO_STATION_CHRKZ,
    "phone": "+74951234567",
    "date": "22.12.2025",
    "duration": RENT_DURATION_ONE_DAY,
    "color": COLOR_CHECKBOX_BLACK,
    "comment": "Ели мясо мужики"
}

CLIENT_DATA_2 = {
    "first_name": "Пётр",
    "last_name": "Петров",
    "address": "Москва, Преображенская площадь, д. 10",
    "metro_station": METRO_STATION_PREOBR_SQR,
    "phone": "89998887766",
    "date": "24.12.2025",
    "duration": RENT_DURATION_TWO_DAYS,
    "color": COLOR_CHECKBOX_GREY,
    "comment": "Пивом запивали"
}