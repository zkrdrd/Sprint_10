import allure

from helpers.data import Address
from pages.base_page import BasePage
from pages.locators import MainPageLocator


class MainPage(BasePage):

    @allure.step("Ввод адреса 'Куда'")
    def input_to(self):
        return self.input_text(MainPageLocator.INPUT_TO, Address.ZUBOVSKY_BOULEVARD_37)

    @allure.step("Ввод адреса 'Откуда'")
    def input_from_is_to(self):
        return self.input_text(
            MainPageLocator.INPUT_FROM, Address.ZUBOVSKY_BOULEVARD_37
        )

    @allure.step("Ввод адреса 'Откуда'")
    def input_from(self):
        return self.input_text(
            MainPageLocator.INPUT_FROM, Address.KHAMOVNICHESKIY_VAL_34
        )

    def route_points_is_displayed(self):
        return self.is_element_present(MainPageLocator.ROUTE_POINTS)

    # def point_b_is_displayed(self):
    #     return self.visibility_element(MainPageLocator.B_POINT)

    def get_map_position(self):
        return self.get_element_position(MainPageLocator.MAP)

    def get_workflow_position(self):
        return self.get_element_position(MainPageLocator.WORKFLOW)
