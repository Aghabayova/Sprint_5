import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import RegistrationPageLocators, LoginPageLocators
from conftest import driver

from data import REGISTRATION_DATA, URLS


def test_registration_successful(driver):
    driver.get(URLS["base"] + URLS["register"])
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_FIELD))

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(REGISTRATION_DATA["valid"]["name"])
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(REGISTRATION_DATA["valid"]["email"])
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_DATA["valid"]["password"])
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Verify successful registration
    WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    # login with registered data

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(REGISTRATION_DATA["valid"]["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(REGISTRATION_DATA["valid"]["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # Verify successful login
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.PLACING_ORDER_BUTTON))


def test_registration_invalid_password(driver):
    driver.get(URLS["base"] + URLS["register"])
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_FIELD))

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(REGISTRATION_DATA["invalid_password"]["name"])
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(REGISTRATION_DATA["invalid_password"]["email"])
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(
        REGISTRATION_DATA["invalid_password"]["password"])
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    # Verify password error
    assert driver.find_element(
        *RegistrationPageLocators.PASSWORD_ERROR).text == RegistrationPageLocators.ERROR_MESSAGE_TEXT
