from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, "//fieldset[1]//input")
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input")
    PASSWORD_FIELD = (By.XPATH, "//fieldset[3]//input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    ERROR_MESSAGE_TEXT = 'Некорректный пароль'


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_BUTTON_FROM_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    USER_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    PLACING_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_BUTTON_FROM_REGISTRATION_FORM = (By.XPATH, "//p[contains(text(), 'Уже зарегистрированы?')]//a["
                                                     "@class='Auth_link__1fOlj']")
    LOGIN_BUTTON_FROM_RESTORE_PASSWORD_FORM = (By.XPATH, "//p[contains(text(), 'Вспомнили пароль?')]//a["
                                                         "@class='Auth_link__1fOlj']")


class UserAccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")


class ConstructorPageLocators:
    BUN_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']")
    BUN_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, '2BEP')]")  # buns tab when selected
    SAUCE_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, '2BEP')]")  # sauces tab when selected
    FILLINGS_ACTIVE_BUTTON = (
        By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, '2BEP')]")  # fillings tab when selected
    H1_LOCATOR = (By.XPATH, '//h1')
