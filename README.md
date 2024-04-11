# Mystore
## Описание
Создан Карпенко Владимиром в процессе изучения фреймфорка Django. Моделирует поведение полноценного интернет магазина-одежды.
## Технологии, используемые в проекте
* Python 3.11
* Django 
* PostgreSQL
* SQLite
## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VladimirKarpenkoMain/mystore
```

```
cd mystore
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Добавить свои значения в .env

```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=5432

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

UKASSA_ID=
UKASSA_SECRET_KEY=

GITHUB_CLIENT_ID=
GITHUB_SECRET_KEY=
```
Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

