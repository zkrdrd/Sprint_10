"""Сценарий. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда",
     выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси

Тебе нужно проверить:

    * Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука,
        нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины (проверить элементы по ТЗ)
    * Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа (проверить элементы по ТЗ)
    * Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа
    * Нажать кнопку Отмена - Окно закрывается
"""

import allure

from pages import CompletedTaxiOrderPage, DetailPage, OrderTaxiPage, WaitingTaxiPage


class TestCallTaxi:

    @allure.title(
        "Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, \
        нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины (проверить элементы по ТЗ)"
    )
    def test_check_waiting_window(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_worker()
        ot.click_requirements_order()
        ot.click_laptop_table()
        ot.click_call_taxi()
        wt = WaitingTaxiPage(order_taxi)
        assert wt.widnow_waiting_taxi_is_displayed()
        assert wt.find_car_is_displayed()
        assert wt.timer_is_displayed()
        assert wt.check_timer_right_position()
        assert wt.cancel_btn_is_displayed()
        assert wt.detail_btn_is_displayed()

    @allure.title("Дождаться окончания таймера поиска машины - \
        Отображается окно совершенного заказа (проверить элементы по ТЗ)")
    def test_complated_order(self, order_taxi):
        OrderTaxiPage(order_taxi).click_call_taxi()
        wt = WaitingTaxiPage(order_taxi)
        wt.waiting()
        cto = CompletedTaxiOrderPage(order_taxi)
        assert cto.title_is_present()
        assert cto.number_is_present()
        assert cto.tarif_image_is_present()
        assert cto.friver_photo_is_present()
        assert cto.driver_rating_is_present()
        assert cto.driver_name_is_present()
        assert cto.cancel_btn_is_present()
        assert cto.detail_btn_is_present()

    @allure.title(
        "Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа"
    )
    def test_complated_order_price(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        price = ot.get_price()
        ot.click_call_taxi()
        wt = WaitingTaxiPage(order_taxi)
        wt.waiting()
        cto = CompletedTaxiOrderPage(order_taxi)
        cto.click_detail_btn()
        dp = DetailPage(order_taxi)
        assert price.join(" ") in dp.get_price()

    @allure.title("Нажать кнопку Отмена - Окно закрывается")
    def test_complated_order_close(self, order_taxi):
        OrderTaxiPage(order_taxi).click_call_taxi()
        wt = WaitingTaxiPage(order_taxi)
        wt.waiting()
        cto = CompletedTaxiOrderPage(order_taxi)
        cto.click_cancel_btn()
        assert cto.order_body_is_closed()
