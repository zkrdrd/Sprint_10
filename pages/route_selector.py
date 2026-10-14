import allure

from helpers import ExpectedString
from pages import BasePage, RouteSelectionLocator


class RouteSelectorPage(BasePage):

    def get_price(self) -> str:
        return self.get_text(RouteSelectionLocator.PRICE)

    def get_time(self) -> str:
        return self.get_text(RouteSelectionLocator.TIME)

    def check_route_price(self) -> bool:
        return self.get_price() == ExpectedString.WALK_PRICE

    def check_route_time(self) -> bool:
        return self.get_time() == ExpectedString.WALK_TIME

    @allure.step("Нажимаем тариф 'Свой'")
    def click_mine(self):
        self.click(RouteSelectionLocator.MINE)

    @allure.step("Нажимаем тариф 'Быстрый'")
    def click_fast(self):
        self.click(RouteSelectionLocator.FAST)

    @allure.step("Нажимаем тариф 'Оптимальный'")
    def click_optimal(self):
        self.click(RouteSelectionLocator.OPTIMAL)

    @allure.step("Нажимаем тариф 'Пешком'")
    def click_walk(self):
        self.click(RouteSelectionLocator.WALK)

    @allure.step("Нажимаем тариф 'Drive'")
    def click_drive(self):
        self.click(RouteSelectionLocator.DRIVE)

    @allure.step("Нажимаем тариф 'Заказать'")
    def click_call_taxi(self):
        self.click(RouteSelectionLocator.BTN_CALL_TAXI)

    def car_is_active(self):
        return self.element_enabled(RouteSelectionLocator.CAR)

    def walk_is_active(self):
        return self.element_enabled(RouteSelectionLocator.WALK)

    def taxi_is_active(self):
        return self.element_enabled(RouteSelectionLocator.TAXI)

    def bike_is_active(self):
        return self.element_enabled(RouteSelectionLocator.BIKE)

    def scooter_is_active(self):
        return self.element_enabled(RouteSelectionLocator.SCOOTER)

    def drive_is_active(self):
        return self.element_enabled(RouteSelectionLocator.DRIVE)

    def optimal_is_selected(self):
        return self.visibility_element(RouteSelectionLocator.ACTIVE_OPTIMAL)

    def fast_is_selected(self):
        return self.visibility_element(RouteSelectionLocator.ACTIVE_FAST)

    def btn_call_taxi_is_clickable(self):
        return self.element_clickable(RouteSelectionLocator.BTN_CALL_TAXI)

    def btn_reserve_is_clickable(self):
        return self.element_clickable(RouteSelectionLocator.BTN_RESERVE)

    def route_selector_is_displayed(self):
        return self.is_element_present(RouteSelectionLocator.BLOCK_SELECT_ROUTE)
