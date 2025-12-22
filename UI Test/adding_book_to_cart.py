from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

# Тест: Добавление книги в корзину
@allure.feature('Корзина')
@allure.story('Добавление книги в корзину')
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.maximize_window()
    driver.quit()

    # Ожидание и клик на первую книгу на главной странице
    with allure.step('Добавляем книгу из главной страницы'):
        wait = WebDriverWait(driver, 15)
        book = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product need-watch product_labeled watched gtm-watched'][@data-position='1']")))
        book.click()

    # Ожидание и клик на кнопку "Добавить в корзину"
    with allure.step('Добавляем книгу в корзину'):
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='buy-button button']")))
        button = driver.find_element(By.XPATH, "//button[@class='buy-button button']")
        button.click()

    # Проверка, что книга добавлена в корзину
    with allure.step('Проверяем, что книга добавлена в корзину'):
        cart_count = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.header-cart-count')))
        assert int(cart_count.text) > 0, "Книга не добавлена в корзину"


