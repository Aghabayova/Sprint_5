from locators import LoginPageLocators, ConstructorPageLocators
from data import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSwitchConstructorTabs:
    def test_click_constructor_bun_tab_success(self, driver):
        driver.get(URLS["base"])
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.H1_LOCATOR, 'Соберите бургер'))

        # Click on Sauces tab
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)).click()

        # Click on Buns tab
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ConstructorPageLocators.BUN_TAB)).click()

        # Verify that the Buns tab is active
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(ConstructorPageLocators.BUN_ACTIVE_BUTTON)
        )
        assert driver.find_element(*ConstructorPageLocators.BUN_ACTIVE_BUTTON).is_displayed()

    def test_click_constructor_sauce_tab_success(self, driver):
        driver.get(URLS["base"])
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.H1_LOCATOR, 'Соберите бургер'))

        # Click on Sauces tab
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)).click()

        # Verify that the Sauces tab is active
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(ConstructorPageLocators.SAUCE_ACTIVE_BUTTON)
        )

        assert driver.find_element(*ConstructorPageLocators.SAUCE_ACTIVE_BUTTON)

    def test_click_constructor_fillings_tab_success(self, driver):
        driver.get(URLS["base"])

        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.H1_LOCATOR, 'Соберите бургер'))

        # Click on Fillings tab
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ConstructorPageLocators.FILLING_TAB)).click()

        # Verify that the Sauces tab is active
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(ConstructorPageLocators.FILLINGS_ACTIVE_BUTTON)
        )

        assert driver.find_element(*ConstructorPageLocators.FILLINGS_ACTIVE_BUTTON)
