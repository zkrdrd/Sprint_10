from pages.main_page import MainPage


class TestMainPage:

    def test_positions(self, driver):
        """Проверка того что карта находится справа"""
        mp = MainPage(driver)
        assert mp.get_workflow_position()["x"] < mp.get_map_position()["x"]

    def test_visible_point_route(self, driver):
        mp = MainPage(driver)
        mp.input_to()
        mp.input_from_is_to()
        assert mp.route_points_is_displayed()
