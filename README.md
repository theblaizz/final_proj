Проект final_proj — это набор автоматизированных тестов на Python для проверки:
API (REST-интерфейсы) — отправка запросов, проверка ответов, схем, кодов состояния.
UI (интерфейс пользователя) — браузерные тесты .
UI + API — возможно объединение проверок на разных уровнях.
Цель: автоматизировать проверку качества и работоспособности как API, так и пользовательского интерфейса веб-приложения.

2) Примеры команд для запуска
Обычно для Python-проекта:

# клонировать репозиторий
git clone https://github.com/theblaizz/final_proj.git
cd final_proj
# создать виртуальное окружение
python -m venv venv
# активировать
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
# установить зависимости
pip install -r requirements.txt

Если requirements.txt нет, зависимости устанавливаются вручную (pytest, selenium, requests и др.).

Запуск всех тестов
pytest
Или:
python -m pytest

Запуск только API-тестов
Если структура содержит папку api_tests или файлы с префиксом api, то:

pytest tests/api
или
pytest -k "api"

Запуск UI-тестов
Если UI-тесты лежат, например, в папке ui_tests:
pytest tests/ui

Для UI-тестов, вероятно, используется Selenium/WebDriver, поэтому должен быть установлен браузерный драйвер (ChromeDriver, GeckoDriver):
# Windows: скачать chromedriver.exe и положить в PATH
