# MyStore

**MyStore** — это интернет-магазин одежды, разработанный с использованием Django и PostgreSQL. Проект включает базовую функциональность интернет-магазина, такую как каталог товаров, корзина покупок, система оплаты (поддержка ЮKassa) и панель администрирования.

## Функциональные особенности

- **Каталог товаров:** Включает в себя категории, фильтрацию и подробные страницы товаров.
- **Корзина покупок:** Добавление, удаление и изменение количества товаров.
- **Система оформления заказа:** Поддержка многошагового процесса оформления заказа.
- **Поддержка онлайн-оплаты:** Интеграция с ЮKassa для приема платежей.
- **Панель администрирования:** Удобное управление товарами, заказами и пользователями через стандартную админку Django.
- **Авторизация через GitHub**

## Технологии

- **Backend:** Django (Python), PostgreSQL
- **Frontend:** HTML, CSS
- **Платежная система:** ЮKassa
- **Авторизация через соцсети:** GitHub (с использованием `django-allauth`)
  
## Как запустить проект

### Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/VladimirKarpenkoMain/mystore.git
    cd mystore
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```
4. Настройте базу данных, почту в `.env`:

    ```
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    ```

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

6. Создайте суперпользователя для доступа к админке:

    ```bash
    python manage.py createsuperuser
    ```

7. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```
### Настройка ЮKassa

1. Зарегистрируйтесь в [ЮKassa](https://yookassa.ru) и получите необходимые параметры (ukassa_id, ukassa_secret_key).

2. Добавьте параметры в файл `.env`:

    ```
    UKASSA_ID=
    UKASSA_SECRET_KEY=
    ```
### Настройка авторизации через GitHub

1. Создайте OAuth-приложение на [GitHub](https://github.com/settings/applications/new) и получите Client ID и Client Secret.

2. Добавьте параметры в файл `.env`:

    ```
    GITHUB_CLIENT_ID=
    GITHUB_SECRET_KEY=
    ```
