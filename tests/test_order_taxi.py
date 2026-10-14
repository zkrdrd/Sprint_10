"""Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля "Откуда" и "Куда",
    выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси

Тебе нужно проверить:

    * Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный
    * При наведении на иконку i в правом верхнем углу каждого тарифа отображается
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ
    * Под тарифами отображается блок с полями Телефон, Способ оплаты,
        Комментарий водителю, Требования к заказу Заказ тарифа Такси.
"""

import allure
import pytest

from pages import OrderTaxiPage, TaxiCardsPage


class TestOrderTaxi:

    @allure.title(
        "Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный"
    )
    def test_open_order_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        assert ot.woker_is_display()
        assert ot.wakation_is_display()
        assert ot.talkative_is_display()
        assert ot.sleepy_is_display()
        assert ot.comforting_is_display()
        assert ot.glosy_is_display()
        assert ot.worker_is_active()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Рабочий' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    def test_worked_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_worker()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.worked_card_is_display()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Отпускной' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    def test_wakation_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_wakation()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.wacation_card_is_display()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Разговорчивый' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    @pytest.mark.xfail(reason="Bug")
    def test_talkative_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_talkative()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.talkative_card_is_display()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Сонный' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    @pytest.mark.xfail(reason="Bug")
    def test_sleepy_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_sleepy()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.sleepy_card_is_display()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Утешительный' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    def test_comforting_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_comforting()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.comforting_card_is_display()

    @allure.title(
        "При наведении на иконку i в правом верхнем углу тарифа 'Глянцевый' отображается \
        всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    def test_glosy_tarif_description_is_right(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_glosy()
        ot.check_card_info()
        tc = TaxiCardsPage(order_taxi)
        assert tc.glossy_card_is_display()

    @allure.title(
        "Под тарифом 'Рабочий' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_worked_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_worker()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()

    @allure.title(
        "Под тарифом 'Отпускной' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_wakation_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_wakation()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()

    @allure.title(
        "Под тарифом 'Разговорчивый' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_talkative_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_talkative()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()

    @allure.title(
        "Под тарифом 'Сонный' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_sleepy_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_sleepy()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()

    @allure.title(
        "Под тарифом 'Утешительный' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_comforting_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_comforting()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()

    @allure.title(
        "Под тарифом 'Глянцевый' отображается блок с полями Телефон, Способ оплаты,\
        Комментарий водителю, Требования к заказу Заказ тарифа Такси."
    )
    def test_glosy_tarif_form(self, order_taxi):
        ot = OrderTaxiPage(order_taxi)
        ot.click_glosy()
        assert ot.phone_field_is_displayed()
        assert ot.payment_method_field_is_displayed()
        assert ot.comment_field_is_displayed()
        assert ot.requirements_field_is_displayed()
