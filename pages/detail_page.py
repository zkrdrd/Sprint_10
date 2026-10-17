from pages import BasePage
from pages.locators import DetailLocator


class DetailPage(BasePage):

    def from_is_present(self):
        return self.is_element_present(DetailLocator.FROM)

    def to_is_present(self):
        return self.is_element_present(DetailLocator.TO)

    def payment_method_is_present(self):
        return self.is_element_present(DetailLocator.PAYMENT_METHOD)

    def price_is_present(self):
        return self.is_element_present(DetailLocator.PRICE)

    def get_from(self):
        return self.get_text(DetailLocator.FROM)

    def get_to(self):
        return self.get_text(DetailLocator.TO)

    def get_payment_method(self):
        return self.get_text(DetailLocator.PAYMENT_METHOD)

    def get_price(self):
        return self.get_text(DetailLocator.PRICE)
