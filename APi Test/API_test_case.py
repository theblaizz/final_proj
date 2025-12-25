import pytest
import requests

BASE_URL = "https://www.labirint.ru"  # Основной URL сайта


# 1. Тест: Проверка доступности главной страницы API
def test_homepage_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


# 2. Тест: Получение списка книг по категории
@pytest.mark.parametrize("category", ["fiction", "non-fiction", "children"])
def test_search_html_contains_book():
    search_term = "Три товарища"
    url = f"{BASE_URL}/search/?q={search_term}"
    response = requests.get(url)
    assert response.status_code == 200
    assert search_term.lower() in response.text.lower()


# 3. Тест: Получение информации о конкретной книге
def test_get_book_info():
    # Используем ID книги для получения данных о ней (например, ID книги с названием "Три товарища")
    book_id = 476703
    url = f"{BASE_URL}/product/{book_id}/"
    response = requests.get(url)
    assert response.status_code == 200,


# 4. Тест: Авторизация пользователя (если есть API для этого)
# Замените значения для теста, если требуется (логин/пароль)
def test_user_login():
    login_url = f"{BASE_URL}/api/v1/auth/login"
    credentials = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = requests.post(login_url, data=credentials)

    assert response.status_code == 200


# 5. Тест: Поиск книги по названию
def test_search_book_by_title():
    search_term = "Три товарища"
    search_url = f"{BASE_URL}/search/?q={search_term}"
    response = requests.get(search_url)

    assert response.status_code == 200,

    # Проверяем, что результаты поиска содержат нужную книгу
    data = response.json()
    assert len(data["products"]) > 0, "No products found in the search results"
    book_titles = [product["title"] for product in data["products"]]
    assert any(
        search_term in title for title in book_titles), f"Book with title '{search_term}' not found in search results"