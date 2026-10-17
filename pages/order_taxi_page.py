import allure

from pages import BasePage, OrderTaxiLocator


class OrderTaxiPage(BasePage):

    def worker_is_active(self):
        return self.element_enabled(OrderTaxiLocator.WORKER)

    def woker_is_display(self):
        return self.is_element_present(OrderTaxiLocator.WORKER)

    def wakation_is_display(self):
        return self.is_element_present(OrderTaxiLocator.WACATION)

    def talkative_is_display(self):
        return self.is_element_present(OrderTaxiLocator.TALKATIVE)

    def sleepy_is_display(self):
        return self.is_element_present(OrderTaxiLocator.SLEEPY)

    def comforting_is_display(self):
        return self.is_element_present(OrderTaxiLocator.COMFORTING)

    def glosy_is_display(self):
        return self.is_element_present(OrderTaxiLocator.GLOSSY)

    @allure.step("Нажимаем на тариф 'Рабочий'")
    def click_worker(self):
        self.click(OrderTaxiLocator.WORKER)

    @allure.step("Нажимаем на тариф 'Отпускной'")
    def click_wakation(self):
        self.click(OrderTaxiLocator.WACATION)

    @allure.step("Нажимаем на тариф 'Разговорчивый'")
    def click_talkative(self):
        self.click(OrderTaxiLocator.TALKATIVE)

    @allure.step("Нажимаем на тариф 'Сонный'")
    def click_sleepy(self):
        self.click(OrderTaxiLocator.SLEEPY)

    @allure.step("Нажимаем на тариф 'Утешительный'")
    def click_comforting(self):
        self.click(OrderTaxiLocator.COMFORTING)

    @allure.step("Нажимаем на тариф 'Глянцевый'")
    def click_glosy(self):
        self.click(OrderTaxiLocator.GLOSSY)

    @allure.step("Нажимаем копку 'Ввести номер и заказать'")
    def click_call_taxi(self):
        self.click(OrderTaxiLocator.CALL_TAXI)

    @allure.step("Нажимаем копку 'Требования к заказу'")
    def click_requirements_order(self):
        self.click(OrderTaxiLocator.REQUIREMENTS)

    @allure.step("Нажимаем копку 'Столик для ноутбука'")
    def click_laptop_table(self):
        self.click(OrderTaxiLocator.LAPTOP_TABLE)

    @allure.step("Наводимся на икноку i")
    def check_card_info(self):
        self.hover_element(OrderTaxiLocator.CARDS_BTN)

    def phone_field_is_displayed(self):
        return self.is_element_present(OrderTaxiLocator.PHONE)

    def payment_method_field_is_displayed(self):
        return self.is_element_present(OrderTaxiLocator.PAYMENT_METHOD)

    def comment_field_is_displayed(self):
        return self.is_element_present(OrderTaxiLocator.COMMENT)

    def requirements_field_is_displayed(self):
        return self.is_element_present(OrderTaxiLocator.REQUIREMENTS)

    def get_price(self):
        return self.get_text(OrderTaxiLocator.PRICE)
