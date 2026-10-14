"""Отрисовка маршрута:

Тебе нужно проверить:

    При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда"
        на карте отображаются две точки начала и конца маршрута
"""

import allure

from pages import MainPage


class TestMainPage:

    def test_positions(self, driver):
        """Проверка того что карта находится справа"""
        mp = MainPage(driver)
        assert mp.get_workflow_position()["x"] < mp.get_map_position()["x"]

    @allure.title('При вводе двух разных адресов в поля "Откуда" и "Куда" \
        на карте отображаются две точки начала и конца маршрута')
    def test_route_points_is_display(self, driver):
        """Проверка отображения точек 'A', 'B' на карте"""
        mp = MainPage(driver)
        mp.input_to_zubovsky_boulevard_37()
        mp.input_from_khamovnicheskiy_val_34()
        assert mp.route_points_is_displayed()
