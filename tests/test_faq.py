import pytest
from pages.main_page import MainPage
from locators.main_page_locators import *
from data import FAQ_ANSWERS

FAQ_TEST_DATA = [
    (FAQ1_PRICE_QUESTION, FAQ1_PRICE_ANSWER, 1),
    (FAQ2_SEVERAL_SCOOTERS_QUESTION, FAQ2_SEVERAL_SCOOTERS_ANSWER, 2),
    (FAQ3_RENT_TIME_QUESTION, FAQ3_RENT_TIME_ANSWER, 3),
    (FAQ4_TODAY_QUESTION, FAQ4_TODAY_ANSWER, 4),
    (FAQ5_EXTEND_ORDER_QUESTION, FAQ5_EXTEND_ORDER_ANSWER, 5),
    (FAQ6_CHARGER_QUESTION, FAQ6_CHARGER_ANSWER, 6),
    (FAQ7_CANCEL_ORDER_QUESTION, FAQ7_CANCEL_ORDER_ANSWER, 7),
    (FAQ8_BEYOND_MKAD_QUESTION, FAQ8_BEYOND_MKAD_ANSWER, 8),
]

@pytest.mark.parametrize("question_locator, answer_locator, faq_number", FAQ_TEST_DATA)
def test_faq_answers(driver, question_locator, answer_locator, faq_number):
    page = MainPage(driver)
    page.accept_cookies()
    page.click_faq_question(question_locator)
    answer_text = page.get_faq_answer(answer_locator)
    assert FAQ_ANSWERS[faq_number] in answer_text