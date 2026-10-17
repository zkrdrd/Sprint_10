from pages.base_page import BasePage
from pages.completed_taxi_order_page import CompletedTaxiOrderPage
from pages.detail_page import DetailPage
from pages.locators import (
    CompletedDriveOrderLocator,
    CompletedTaxiOrderLocator,
    DetailLocator,
    DriveCardsLocator,
    DriveLicenseLocator,
    DriveOrderLocator,
    MainPageLocator,
    OrderTaxiLocator,
    RouteSelectionLocator,
    TaxiCardsLocator,
    WaitingTaxiLocator,
)
from pages.main_page import MainPage
from pages.order_taxi_page import OrderTaxiPage
from pages.route_selector import RouteSelectorPage
from pages.taxi_card_page import TaxiCardsPage
from pages.waiting_taxi_page import WaitingTaxiPage

__all__ = [
    "MainPageLocator",
    "RouteSelectionLocator",
    "OrderTaxiLocator",
    "TaxiCardsLocator",
    "WaitingTaxiLocator",
    "DetailLocator",
    "CompletedTaxiOrderLocator",
    "DriveOrderLocator",
    "DriveCardsLocator",
    "DriveLicenseLocator",
    "CompletedDriveOrderLocator",
    "BasePage",
    "MainPage",
    "RouteSelectorPage",
    "OrderTaxiPage",
    "TaxiCardsPage",
    "WaitingTaxiPage",
    "CompletedTaxiOrderPage",
    "DetailPage",
]
