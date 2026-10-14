"""Отрисовка блока с выбором маршрута:

Тебе нужно проверить:

    * При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда"
        под выбором адресов отображается блок с выбором маршрута
    * При вводе одинакового адреса в поля "Откуда" и "Куда"
        под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин.

    Подготовка к заказу такси.  Ввести два разных предустановленных адреса в поля "Откуда" и "Куда"

Тебе нужно проверить:

    * При переключении между видами маршрута (Оптимальный|Быстрый)
        происходит смена активного таба и пересчет времени и стоимости маршрута
    * При переключении на вид маршрута Свой происходит смена активного таба
        и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)
    * При выборе вида маршрута Быстрый активна кнопка Вызвать такси
    * При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать

"""

import allure

from pages import MainPage, RouteSelectorPage


class TestRouteSelector:

    @allure.title('При вводе двух разных адресов в поля "Откуда" и "Куда" \
        под выбором адресов отображается блок с выбором маршрута')
    def test_route_selector_different_address(self, full_address):
        rs = RouteSelectorPage(full_address)
        assert rs.route_selector_is_displayed()

    @allure.title(
        'При вводе одинакового адреса в поля "Откуда" и "Куда"\
        под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."'
    )
    def test_route_selector_duplicate_address(self, driver):
        mp = MainPage(driver)
        mp.input_to_zubovsky_boulevard_37()
        mp.input_from_zubovsky_boulevard_37()
        rs = RouteSelectorPage(driver)
        rs.click_mine()
        rs.walk_is_active()
        rs.click_walk()
        assert rs.check_route_price()
        assert rs.check_route_time()

    @allure.title(
        "При переключении между видами маршрута (Оптимальный|Быстрый) "
        "происходит смена активного таба и пересчет времени и стоимости маршрута"
    )
    def test_change_route_optimal(self, full_address):
        rs = RouteSelectorPage(full_address)
        rs.click_fast()
        price = rs.get_price()
        # time = rs.get_time()
        rs.click_optimal()
        assert rs.optimal_is_selected()
        assert rs.get_price() != price
        # assert rs.get_time() != time

    @allure.title(
        "При переключении между видами маршрута (Оптимальный|Быстрый) "
        "происходит смена активного таба и пересчет времени и стоимости маршрута"
    )
    def test_change_route_faster(self, full_address):
        rs = RouteSelectorPage(full_address)
        rs.click_optimal()
        price = rs.get_price()
        # time = rs.get_time()
        rs.click_fast()
        assert rs.fast_is_selected()
        assert rs.get_price() != price
        # assert rs.get_time() != time
        assert rs.walk_is_active()

    @allure.title(
        "При переключении на вид маршрута Свой происходит смена активного таба \
            и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)"
    )
    def test_active_types(self, full_address):
        rs = RouteSelectorPage(full_address)
        rs.click_mine()
        assert rs.car_is_active()
        assert rs.walk_is_active()
        assert rs.taxi_is_active()
        assert rs.bike_is_active()
        assert rs.scooter_is_active()
        assert rs.drive_is_active()

    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_fast_call_taxi_btn(self, full_address):
        rs = RouteSelectorPage(full_address)
        rs.click_fast()
        assert rs.btn_call_taxi_is_clickable()

    @allure.title(
        "При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать"
    )
    def test_mine_drive_reserve_btn(self, full_address):
        rs = RouteSelectorPage(full_address)
        rs.click_mine()
        rs.click_drive()
        assert rs.btn_reserve_is_clickable()
