import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.maximize_window()
    driver.quit()

@pytest.fixture
def base_url() -> str:
    return 'https://reqres.in/'