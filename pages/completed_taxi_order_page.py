import allure

from pages import BasePage
from pages.locators import CompletedTaxiOrderLocator


class CompletedTaxiOrderPage(BasePage):

    def order_body_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.ORDER_BODY)

    def order_body_is_closed(self) -> bool:
        return self.is_closed(CompletedTaxiOrderLocator.ORDER_BODY)

    def title_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.TITLE)

    def number_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.NUMBER)

    def tarif_image_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.TARIF_IMAGE)

    def friver_photo_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.DRIVER_PHOTO)

    def driver_rating_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.DRIVER_RATING)

    def driver_name_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.DRIVER_NAME)

    def cancel_btn_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.CANCEL_BTN)

    def detail_btn_is_present(self) -> bool:
        return self.is_element_present(CompletedTaxiOrderLocator.DETAIL_BTN)

    @allure.step("Нажимаем на кнопку 'Отменить'")
    def click_cancel_btn(self):
        self.click(CompletedTaxiOrderLocator.CANCEL_BTN)

    @allure.step("Нажимаем на кнопку 'Детали'")
    def click_detail_btn(self):
        self.click(CompletedTaxiOrderLocator.DETAIL_BTN)
