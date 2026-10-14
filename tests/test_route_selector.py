from pages.main_page import MainPage
from pages.route_selector import RouteSelectorPage


class TestRouteSelector:
    def test_route_selector_different_address(self, driver):
        mp = MainPage(driver)
        mp.input_to()
        mp.input_from()
        rs = RouteSelectorPage(driver)
        assert rs.route_selector_is_displayed()

    def test_route_selector_duplicate_address(self, driver):
        mp = MainPage(driver)
        mp.input_to()
        mp.input_from_is_to()
        rs = RouteSelectorPage(driver)
        assert rs.auto_free_wait_zero_min()
