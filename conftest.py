# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
