import allure

from helpers import Address
from pages import BasePage, MainPageLocator


class MainPage(BasePage):

    @allure.step("Ввод адреса 'Куда'")
    def input_to_zubovsky_boulevard_37(self):
        return self.input_text(MainPageLocator.INPUT_TO, Address.ZUBOVSKY_BOULEVARD_37)

    @allure.step("Ввод адреса 'Откуда'")
    def input_from_zubovsky_boulevard_37(self):
        return self.input_text(
            MainPageLocator.INPUT_FROM, Address.ZUBOVSKY_BOULEVARD_37
        )

    @allure.step("Ввод адреса 'Откуда'")
    def input_from_khamovnicheskiy_val_34(self):
        return self.input_text(
            MainPageLocator.INPUT_FROM, Address.KHAMOVNICHESKIY_VAL_34
        )

    def route_points_is_displayed(self):
        return self.is_element_present(MainPageLocator.ROUTE_POINTS)

    def get_map_position(self):
        return self.get_element_position(MainPageLocator.MAP)

    def get_workflow_position(self):
        return self.get_element_position(MainPageLocator.WORKFLOW)
