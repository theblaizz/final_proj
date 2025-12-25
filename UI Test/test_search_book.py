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

# Тест: Поиск книги
@allure.feature('Поиск книги')
@allure.story('Поиск книги по названию')
@allure.title('Проверка поиска по названию "Три товарища"')
def test_search_book(driver):
    with allure.step('Вводим название книги в поисковое поле'):
        search_box = driver.find_element_by_name("search")
        search_box.send_keys("Три товарища")
        search_box.send_keys(Keys.RETURN)

    with allure.step('Ожидаем появления результатов поиска'):
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-title'))
        )

    with allure.step('Проверяем, что результаты поиска отображаются'):
        results = driver.find_elements_by_css_selector('.product-title')
        assert len(results) > 0, "Результаты поиска не отображаются"