import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from helpers.data import URL
from pages import MainPage, RouteSelectorPage


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def full_address(driver):
    mp = MainPage(driver)
    mp.input_to_zubovsky_boulevard_37()
    mp.input_from_khamovnicheskiy_val_34()
    return driver


@pytest.fixture()
def order_taxi(full_address):
    rs = RouteSelectorPage(full_address)
    rs.click_fast()
    rs.click_call_taxi()
    return full_address
