from pages import BasePage, WaitingTaxiLocator


class WaitingTaxiPage(BasePage):

    def widnow_waiting_taxi_is_displayed(self) -> bool:
        return self.is_element_present(WaitingTaxiLocator.WINDOW_WAITING_TAXI)

    def find_car_is_displayed(self) -> bool:
        return self.is_element_present(WaitingTaxiLocator.FIND_CAR)

    def timer_is_displayed(self) -> bool:
        return self.is_element_present(WaitingTaxiLocator.TIMER)

    def cancel_btn_is_displayed(self) -> bool:
        return self.is_element_present(WaitingTaxiLocator.CANCEL_BTN)

    def detail_btn_is_displayed(self) -> bool:
        return self.is_element_present(WaitingTaxiLocator.DETAIL_BTN)

    def check_timer_right_position(self) -> bool:
        return (
            self.get_element_position(WaitingTaxiLocator.FIND_CAR)["x"]
            < self.get_element_position(WaitingTaxiLocator.TIMER)["x"]
        )

    def get_timer_text(self) -> int:
        timer = 0
        while timer == 0:
            timer = int(self.get_text(WaitingTaxiLocator.TIMER)[-2:])
        return timer + 1

    def waiting(self):
        self.is_element_present(WaitingTaxiLocator.TIMER)
        self.waiting_time(self.get_timer_text(), WaitingTaxiLocator.TIMER)
