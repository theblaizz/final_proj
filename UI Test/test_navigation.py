import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Тест: Навигация по категориям
@allure.feature('Навигация')
@allure.story('Переход по категориям')
def test_navigation(driver):
    with allure.step('Переходим в раздел "Книги"'):
        category_link = driver.find_element_by_link_text("Книги")
        category_link.click()

    with allure.step('Ожидаем появления списка книг'):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.catalog'))
        )

    with allure.step('Проверяем, что раздел с книгами отображается'):
        books_section = driver.find_element_by_css_selector('.catalog')
        assert books_section.is_displayed(), "Раздел с книгами не найден"
