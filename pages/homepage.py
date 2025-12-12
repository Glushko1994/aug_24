from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get('https://www.demoblaze.com/')
        return self

    def click_galaxy_s6(self):
        # Ищем товар по тексту
        product = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[contains(text(), "Samsung") and contains(text(), "s6")]')
            )
        )
        product.click()
        return self

    def click_monitor(self):
        # Ищем категорию Monitors
        monitor = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[contains(text(), "Monitors")]')
            )
        )
        monitor.click()
        return self

    def check_products_count(self, expected_count):
        # Ждем загрузки товаров
        products = self.wait.until(
            lambda d: d.find_elements(By.CSS_SELECTOR, '.card')
            if len(d.find_elements(By.CSS_SELECTOR, '.card')) > 0
            else False
        )

        assert len(products) == expected_count
        return self




