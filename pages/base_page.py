import allure
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # def open_page(self):
    #     self.driver.get(URL.BASE_URL)
    #     return self

    def visibility_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_element_position(self, locator):
        return self.visibility_element(locator).location

    def element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def upload_image(self, image, *locator):
        self.find_element(*locator).send_keys(image)

    def get_current_url(self):
        return self.driver.current_url

    def execute_script(self, script, source=None, targer=None):
        self.driver.execute_script(script, source, targer)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_text(self, locator):
        return self.visibility_element(locator).text

    @allure.step("Нажимаем кнопку {locator}")
    def click(self, locator):
        self.execute_script("arguments[0].click();", self.element_clickable(locator))

    @allure.step("Вводим текст")
    def input_text(self, locator, text):
        element = self.visibility_element(locator)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
