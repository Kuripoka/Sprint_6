import pytest
from selenium import webdriver
from data import urls


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(urls.SCOOTER_URL)
    yield driver
    driver.quit()