from selenium.webdriver.common.by import By


class MainPageLocator:
    """Блок начального экрана:

    Карта в правой части экрана
    Блок с вводом адресов: Откуда, Куда"""

    MAP = (By.XPATH, "//div[contains(@class, 'map')]")
    WORKFLOW = (By.XPATH, "//div[contains(@class, 'workflow')]")
    INPUT_FROM = (By.XPATH, "//input[contains(@id,'from')]")
    INPUT_TO = (By.XPATH, "//input[contains(@id,'to')]")
    ROUTE_POINTS = (
        By.XPATH,
        "//ymaps[@class='ymaps-2-1-79-placemark-overlay ymaps-2-1-79-user-selection-none']",
    )


class RouteSelectionLocator:
    """Блок с выбором маршрута:

    Виды маршрута: Оптимальный, Быстрый, Свой
    Типы передвижения: Машина, Пешком, Такси, Велосипед, Самокат, Двайв
    Блок информации: Стоимость, Время в пути
    Кнопка Вызвать такси для типа Такси
    Кнопка Забронировать для типа Драйв"""

    # //div[@class='types-container']//div[contains(@class,'type') and not(@disabled)]//img[contains(@src, 'car') and contains(@class, 'type-icon')]

    BLOCK_SELECT_ROUTE = (By.XPATH, "//div[@class='type-picker shown']")
    OPTIMAL = (By.XPATH, "//div[text()='Оптимальный']")
    FAST = (By.XPATH, "//div[text()='Быстрый']")
    MINE = (By.XPATH, "//div[text()='Свой']")
    CAR = (By.XPATH, "//img[contains(@src, 'car') and contains(@class, 'type-icon')]")
    WALK = (By.XPATH, "//img[contains(@src, 'walk') and contains(@class, 'type-icon')]")
    TAXI = (By.XPATH, "//img[contains(@src, 'taxi') and contains(@class, 'type-icon')]")
    BIKE = (By.XPATH, "//img[contains(@src, 'bike') and contains(@class, 'type-icon')]")
    SCOOTER = (
        By.XPATH,
        "//img[contains(@src, 'scooter') and contains(@class, 'type-icon')]",
    )
    DRIVE = (
        By.XPATH,
        "//img[contains(@src, 'drive') and contains(@class, 'type-icon')]",
    )
    PRICE = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]//div[contains(@class, 'text')]",
    )
    TIME = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]//div[contains(@class, 'duration')]",
    )
    CALL_TAXI = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]//button[contains(text(), 'Вызвать такси')]",
    )
    RESERVE = (
        By.XPATH,
        "//div[contains(@class, 'results-text')]//button[contains(text(), 'Забронировать')]",
    )
    BTN_CALL_TAXI = (By.XPATH, "//button[text()='Вызвать такси']")
    BTN_RESERVE = (By.XPATH, "//button[text()='Забронировать']")

    ACTIVE_OPTIMAL = (By.XPATH, "//div[@class='mode active' and text()='Оптимальный']")
    ACTIVE_FAST = (By.XPATH, "//div[@class='mode active' and text()='Быстрый']")


class OrderTaxiLocator:
    """Блок заказа Такси:

    Тарифы: Рабочий, Сонный, Отпускной, Разговорчивый, Утешительный, Глянцевый
    Поля для заполнения: Телефон, Способ оплаты, Комментарий водителю, Требования к заказу
    Кнопка Ввести номер и заказать
    """

    WORKER = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Рабочий']",
    )
    SLEEPY = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Сонный']",
    )
    WACATION = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Отпускной']",
    )
    TALKATIVE = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Разговорчивый']",
    )
    COMFORTING = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Утешительный']",
    )
    GLOSSY = (
        By.XPATH,
        "//div[contains(@class,'tcard')]//following-sibling::div[text()='Глянцевый']",
    )
    PHONE = (By.XPATH, "//div[text()='Телефон']")
    PAYMENT_METHOD = (By.XPATH, "//div[text()='Способ оплаты']")
    COMMENT = (By.XPATH, "//label[text()='Комментарий водителю...']")
    REQUIREMENTS = (By.XPATH, "//div[text()='Требования к заказу']")
    CALL_TAXI = (By.XPATH, "//button[@class='smart-button']")
    CARDS_BTN = (By.XPATH, "//div[@class ='tcard active']//button")
    LAPTOP_TABLE = (
        By.XPATH,
        "//div[@class='r-sw-container'and div[text()='Столик для ноутбука']]//div[@class='switch']",
    )
    PRICE = (By.XPATH, "//div[@class='tcard active']//div[@class='tcard-price']")


class TaxiCardsLocator:
    """Описание тарифов Такси:

    Рабочий - Для деловых особ, которых отвлекают
    Сонный - Для тех, кто не выспался
    Отпускной - Если пришла пора отдохнуть
    Разговорчивый - Если мысли не выходят из головы
    Утешительный - Если хочется свернуться калачиком
    Глянцевый - Если нужно блистать
    """

    WORKED = (
        By.XPATH,
        "//div[@id='tariff-card-0' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Рабочий'] and div[@class='i-floating']/div[text()='Для деловых особ, которых отвлекают']]",
    )
    SLEEPY = (
        By.XPATH,
        "//div[@id='tariff-card-1' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Сонный'] and div[@class='i-floating']/div[text()='Для тех, кто не выспался']]",
    )
    WACATION = (
        By.XPATH,
        "//div[@id='tariff-card-2' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Отпускной'] and div[@class='i-floating']/div[text()='Если пришла пора отдохнуть']]",
    )
    TALKATIVE = (
        By.XPATH,
        "//div[@id='tariff-card-3' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Разговорчивый'] and div[@class='i-floating']/div[text()='Если мысли не выходят из головы']]",
    )
    COMFORTING = (
        By.XPATH,
        "//div[@id='tariff-card-4' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Утешительный'] and div[@class='i-floating']/div[text()='Если хочется свернуться калачиком']]",
    )
    GLOSSY = (
        By.XPATH,
        "//div[@id='tariff-card-5' and contains(@class, 'show') and div[@class='i-floating']/div[text()='Глянцевый'] and div[@class='i-floating']/div[text()='Если нужно блистать']]",
    )


class WaitingTaxiLocator:
    """Окно ожидания машины Такси:

    Заголовок: Поиск машины
    Таймер обратного отсчета в правом верхнем углу
    Кнопки: Отменить, Детали
    """

    WINDOW_WAITING_TAXI = (By.XPATH, "//div[@class='order-body']")
    FIND_CAR = (By.XPATH, "//div[@class='order-body']//div[text()='Поиск машины']")
    TIMER = (By.XPATH, "//div[@class='order-body']//div[@class='order-header-time']")
    CANCEL_BTN = (
        By.XPATH,
        "//div[@class='order-body']//div[text()='Отменить']//preceding-sibling::button",
    )
    DETAIL_BTN = (
        By.XPATH,
        "//div[@class='order-body']//div[text()='Детали']//preceding-sibling::button",
    )


class DetailLocator:
    """Окно Детали:

    Адреса: Адрес подачи, Адрес назначения (указаны адреса введенные в поля Откуда и Куда)
    Способ оплаты (указана информация из поля Способ оплаты из формы заказа Такси)
    Блок информации: заголовок Еще про поездку, информация Стоимость
    """

    FROM = (By.XPATH, "//div[text()='Адрес подачи']//preceding-sibling::div")
    TO = (By.XPATH, "//div[text()='Адрес назначения']//preceding-sibling::div")
    PAYMENT_METHOD = (By.XPATH, "//div[text()='Способ оплаты']//preceding-sibling::div")
    PRICE = (By.XPATH, "//div[text()='Еще про поездку']//following-sibling::div")


class CompletedTaxiOrderLocator:
    """Окно совершенного заказа Такси:

    Заголовок: n мин. и приедет >
    Номер автомобиля и картинка тарифа в правом верхнем углу
    Блок с информацией о водителе: Имя, фото, рейтинг в правом верхнем углу фото
    Кнопки: Отменить, Детали
    """

    ORDER_BODY = (By.XPATH, "//div[@class='order-body']")
    TITLE = (By.XPATH, "//div[@class='order-body']//div[text()=' мин. и приедет']")
    NUMBER = (By.XPATH, "//div[@class='order-body']//div[@class='number']")
    TARIF_IMAGE = (By.XPATH, "//div[@class='order-body']//img[contains(@alt,'Car')]")
    DRIVER_PHOTO = (
        By.XPATH,
        "//div[@class='order-body']//div[@class='order-button']//img",
    )
    DRIVER_RATING = (
        By.XPATH,
        "//div[@class='order-body']//div[@class='order-button']//div[@class='order-btn-rating']",
    )
    DRIVER_NAME = (
        By.XPATH,
        "//div[@class='order-body']//div[@class='order-btn-rating']/../..//following-sibling::div[text()]",
    )
    CANCEL_BTN = (
        By.XPATH,
        "//div[@class='order-body']//div[@class='order-btn-group']//div[text()='Отменить']//preceding-sibling::button",
    )
    DETAIL_BTN = (
        By.XPATH,
        "//div[@class='order-body']//div[@class='order-btn-group']//div[text()='Детали']//preceding-sibling::button",
    )


class DriveOrderLocator:
    """Блок заказа Драйв:

    Тарифы: Повседневный, Походный, Роскошный
    Поля для заполнения: Добавить права, Способ оплаты, Требования к заказу
    Кнопка Ввести права и забронировать
    """

    EVERYDAY = (
        By.XPATH,
        "//div[@class='tariff-cards']//div[@class='tcard-title' and text()='Повседневный']",
    )
    HIKING = (
        By.XPATH,
        "//div[@class='tariff-cards']//div[@class='tcard-title' and text()='Походный']",
    )
    LUXURY = (
        By.XPATH,
        "//div[@class='tariff-cards']//div[@class='tcard-title' and text()='Роскошный']",
    )
    ADD_LICENSE = (By.XPATH, "//div[text()='Добавить права']")
    PAYMENT_METHODS = (
        By.XPATH,
        "//div[@class='pp-button filled']//div[text()='Способ оплаты']",
    )
    REQUIREMENTS_ORDER = (
        By.XPATH,
        "//div[contains(@class,'reqs')]//div[text()='Требования к заказу']",
    )
    RESERVE_BTN = (By.XPATH, "//button[@class='smart-button']")


class DriveCardsLocator:
    """Описание тарифов Драйв:

    Повседневный - BMW 750 Просто по делам, ничего лишнего
    Походный - KIA RIO Для путешествий
    Роскошный - PORSCHE 911 Блеск, мощь, глянец
    """

    EVERYDAY = (
        By.XPATH,
        "//div[text()='BMW 750']//following-sibling::div[text()='Просто по делам, ничего лишнего']",
    )
    HIKING = (
        By.XPATH,
        "//div[text()='Kia Rio']//following-sibling::div[text()='Для путешествий']",
    )
    LUXURY = (
        By.XPATH,
        "//div[text()='Porsche 911']//following-sibling::div[text()='Блеск, мощь, глянец']",
    )


class DriveLicenseLocator:
    """Окно Добавление прав тарифа Драйв:

    Поля для заполнения: Имя, Фамилия, Дата рождения, Номер
    Кнопки: Добавить, Отмена
    """

    FIRST_NAME_INPUT = (
        By.XPATH,
        "//div[@class='section active']//input[@id='firstName']",
    )
    LAST_NAME_INPUT = (
        By.XPATH,
        "//div[@class='section active']//input[@id='lastName']",
    )
    BIRTH_DATE_INPUT = (
        By.XPATH,
        "//div[@class='section active']//input[@id='birthDate']",
    )
    LICENSE_NUMBER_INPUT = (
        By.XPATH,
        "//div[@class='section active']//input[@id='number']",
    )
    ADD_BUTTON = (By.XPATH, "//div[@class='section active']//button[text()='Добавить']")
    CANCEL_BUTTON = (
        By.XPATH,
        "//div[@class='section active']//button[text()='Отмена']",
    )


class CompletedDriveOrderLocator:
    """Окно совершенного заказа Драйв:

    Заголовок: Машина забронирована
    Описание: Бесплатное ожидание и таймер в правом верхнем углу
    Изображение картинки выбранного тарифа и название тарифа над ней
    Кнопка Отменить
    Блок с информацией: Адрес машины (указан адрес введенный в поле Откуда), Еще про поездку (Стоимость)
    """

    RESERVE_DRIVE_HEADER = (
        By.XPATH,
        "//div[@class='order-body']//div[text()='Машина забронирована']",
    )
    FREE_WAITING = (
        By.XPATH,
        "//div[@class='order-body']//div[text()='Бесплатное ожидание']",
    )
    TIMER = (By.XPATH, "//div[@class='order-body']//div[@class='order-header-time']")
    TARIF_NAME = (
        By.XPATH,
        "//div[@class='order-body']//img[@alt='Car']/..//preceding-sibling::div[text()]",
    )
    CAR_IMAGE = (By.XPATH, "//div[@class='order-body']//img[@alt='Car']")
    CANCEL_BUTTON = (By.XPATH, "//div[text()='Отменить']//preceding-sibling::button")
    FROM = (By.XPATH, "//div[text()='Адрес машины']//preceding-sibling::div[text()]")
    PRICE = (
        By.XPATH,
        "//div[text()='Еще про поездку']//following-sibling::div[text()]",
    )
