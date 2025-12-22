from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure

# Фикстура для запуска и завершения драйвера
@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.labirint.ru")
    yield driver
    driver.quit()

    # Тест: Оформление заказа
    @allure.feature('Оформление заказа')
    @allure.story('Оформление заказа через корзину')
    def test_checkout(driver):
        with allure.step('Вводим название книги в поисковое поле'):
            search_box = driver.find_element_by_name("search")
            search_box.send_keys("Три товарища")
            search_box.send_keys(Keys.RETURN)

        with allure.step('Ожидаем появления результатов поиска'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title'))
            )

        with allure.step('Выбираем первую книгу'):
            book = driver.find_element_by_css_selector('.product-title a')
            book.click()

        with allure.step('Добавляем книгу в корзину'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.buy-button'))
            )
            add_to_cart_button = driver.find_element_by_css_selector('.buy-button')
            add_to_cart_button.click()

        with allure.step('Переходим в корзину'):
            cart_button = driver.find_element_by_css_selector('.header-cart-count')
            cart_button.click()

        with allure.step('Проверяем наличие кнопки "Оформить заказ"'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-button'))
            )
            checkout_button = driver.find_element_by_css_selector('.checkout-button')
            assert checkout_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается"

        with allure.step('Нажимаем на кнопку "Оформить заказ"'):
            checkout_button.click()

        with allure.step('Проверяем отображение формы для ввода данных доставки'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "delivery"))
            )
            delivery_section = driver.find_element_by_id("delivery")
            assert delivery_section.is_displayed(), "Форма для ввода данных доставки не появилась"
