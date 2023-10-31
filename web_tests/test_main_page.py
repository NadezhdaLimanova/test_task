

class TestMainPage:
    """Класс для тестирования поисков объектов на главной странице"""

    def test_homepage(self, base_url, driver):
        expected_url = base_url
        driver.get(base_url)
        actual_url = driver.current_url
        assert actual_url == expected_url








