from selenium.webdriver.common.by import By


class MainPageLocator:
    MAP = (By.XPATH, "//div[contains(@class, 'map')]")
    WORKFLOW = (By.XPATH, "//div[contains(@class, 'workflow')]")
    INPUT_FROM = (By.XPATH, "//input[contains(@id,'from')]")
    INPUT_TO = (By.XPATH, "//input[contains(@id,'to')]")
    ROUTE_POINTS = (By.XPATH, "//ymaps[contains(@class,'ymaps-2-1-79-route-pin__b')]")
    # B_POINT = (By.XPATH, "//ymaps[contains(@class,'ymaps-2-1-79-route-pin__b')]")


class RouteSelectorLocator:
    SELECT_ROUTE_BLOCK = (By.XPATH, "//div[contains(@class,'type-picker shown')]")
    OPTIMAL = (By.XPATH, "//div[text()='Оптимальный']")
    FAST = (By.XPATH, "//div[text()='Быстрый']")
    MINE = (By.XPATH, "//div[text()='Свой']")
    AUTO_IS_FREE_WAIT_ZERO_MIN = (
        By.XPATH,
        "//div[text()='Авто Бесплатно']/following-sibling::div[text()='В пути 0 мин.']",
    )
