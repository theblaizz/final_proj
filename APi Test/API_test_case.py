import pytest
import requests

BASE_URL = "https://www.labirint.ru"  # Основной URL сайта


# 1. Тест: Проверка доступности главной страницы API
def test_homepage_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


# 2. Тест: Получение списка книг по категории
@pytest.mark.parametrize("category", ["fiction", "non-fiction", "children"])
def test_get_books_by_category(category):
    url = f"{BASE_URL}/genres/{category}/"
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to get books for category {category}, status code: {response.status_code}"
    assert "books" in response.json(), "Books not found in response"


# 3. Тест: Получение информации о конкретной книге
def test_get_book_info():
    # Используем ID книги для получения данных о ней (например, ID книги с названием "Три товарища")
    book_id = 476703
    url = f"{BASE_URL}/product/{book_id}/"
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to get book info, status code: {response.status_code}"

    # Проверяем, что название книги и цена присутствуют в ответе
    data = response.json()
    assert "title" in data, "Book title is missing in the response"
    assert "price" in data, "Book price is missing in the response"


# 4. Тест: Авторизация пользователя (если есть API для этого)
# Замените значения для теста, если требуется (логин/пароль)
def test_user_login():
    login_url = f"{BASE_URL}/api/v1/auth/login"
    credentials = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = requests.post(login_url, data=credentials)

    assert response.status_code == 200, f"Login failed, status code: {response.status_code}"
    assert "token" in response.json(), "Auth token not found in the response"


# 5. Тест: Поиск книги по названию
def test_search_book_by_title():
    search_term = "Три товарища"
    search_url = f"{BASE_URL}/search/?q={search_term}"
    response = requests.get(search_url)

    assert response.status_code == 200, f"Search failed, status code: {response.status_code}"

    # Проверяем, что результаты поиска содержат нужную книгу
    data = response.json()
    assert len(data["products"]) > 0, "No products found in the search results"
    book_titles = [product["title"] for product in data["products"]]
    assert any(
        search_term in title for title in book_titles), f"Book with title '{search_term}' not found in search results"