from locators import LoginPageLocators, UserAccountPageLocators
from data import LOGIN_DATA, URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigationToConstructor:
    def test_click_constructor_button_success(self, driver):
        driver.get(URLS["base"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON_FROM_MAIN).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(LOGIN_DATA["valid"]["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(LOGIN_DATA["valid"]["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Verify successful login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.PLACING_ORDER_BUTTON))

        driver.find_element(*LoginPageLocators.USER_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/profile"))

        driver.find_element(*UserAccountPageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.PLACING_ORDER_BUTTON))

    def test_click_stellar_burgers_logo_success(self, driver):
        driver.get(URLS["base"])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON_FROM_MAIN).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(LOGIN_DATA["valid"]["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(LOGIN_DATA["valid"]["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Verify successful login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.PLACING_ORDER_BUTTON))

        driver.find_element(*LoginPageLocators.USER_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/profile"))

        driver.find_element(*UserAccountPageLocators.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.PLACING_ORDER_BUTTON))