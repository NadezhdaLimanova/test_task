from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators:
    """Класс для локаторов на главной странице"""

    GET_LIST_USERS_BUTTON = (By.CSS_SELECTOR, '[data-id="users"]')
    LOGO = (By.XPATH, '//h1/a/img')


class BasePage:
    """Класс, определяющий базовые методы для работы с Webdriver"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


