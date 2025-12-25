import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Фикстура для запуска и завершения драйвера
@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.labirint.ru")
    yield driver
    driver.quit()

# Тест: Страница товара
@allure.feature('Страница товара')
@allure.story('Проверка элементов страницы товара')
@allure.title('Вводим название книги')
def test_product_page(driver):
    with allure.step('Вводим название книги в поисковое поле'):
        search_box = driver.find_element_by_name("search")
        search_box.send_keys("Три товарища")
        search_box.send_keys(Keys.RETURN)

    with allure.step('Ожидаем появления результатов поиска'):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title'))
        )

    with allure.step('Переходим на страницу товара'):
        book = driver.find_element_by_css_selector('.product-title a')
        book.click()

    with allure.step('Ожидаем загрузки страницы товара'):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title'))
        )

    with allure.step('Проверяем, что название и цена товара отображаются'):
        title = driver.find_element_by_css_selector('.product-title')
        price = driver.find_element_by_css_selector('.price-val')
        assert title.is_displayed(), "Название книги не отображается"
        assert price.is_displayed(), "Цена книги не отображается"