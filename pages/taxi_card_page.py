from pages import BasePage, TaxiCardsLocator


class TaxiCardsPage(BasePage):
    def worked_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.WORKED)

    def sleepy_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.SLEEPY)

    def wacation_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.WACATION)

    def talkative_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.TALKATIVE)

    def comforting_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.COMFORTING)

    def glossy_card_is_display(self):
        return self.visibility_element(TaxiCardsLocator.GLOSSY)
