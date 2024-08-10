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
    CONSTRUCTOR_BUTTON = (By.XPATH, "//button[text()='Конструктор']")
    PROFILE_IMAGE = (By.CSS_SELECTOR, ".profile__image")


class ConstructorPageLocators:
    BUN_TAB = (By.XPATH, "//tab[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//tab[text()='Соусы']")
    TOPPINGS_TAB = (By.XPATH, "//tab[text()='Начинки']")
