# 1. Интернет-магазин(beta) (catalog app)

## Описание:
Проект реализован через Django фреймворк, содержит:
* Домашнюю страницу `home`
* Страницу с контактами
  * На странице с контактами реализован POST запрос
* Имеются модели для таблиц Product и Category
* Организована админка
* Реализованны кастомные команды:
  * Очистка таблиц от данных `python manage.py to_truncate`
  * Загрузка из ранее сохраненных фикстур через
  ```
  python -Xutf8 manage.py dumpdata catalog.<нужная модель> --output <название фикстуры формата "<имя модели в нижнем регистре>_fixture">.json --indent 4
  ```
  данных в таблицы Product (`python manage.py load_product_fixture`)
  и таблицы Category (`python manage.py load_category_fixture`)
### !!!ВНИМАНИЕ!!!
Перед использованием `python manage.py load_product_fixture` ОБЯЗАТЕЛЬНО необходимо 
провести загрузку `python manage.py load_category_fixture`, иначе будет ошибка

* Добавлен функционал добавления продукта на домашней `home`
* Представления работают на принципах CBV

## Установка
1. Клонировать репозиторий
  ```
  git clone https://github.com/VikVyaz/Django_pr
  ```
2. Установка зависимостей
  ````
  pip install -r requirements.txt
  ````

## Использование

* В консоли прописать `python manage.py runserver` и зайти на сайт
(строка "Starting development server at....." со ссылкой)

* Зайти в админку:
  * провести миграции (`python manage.py makemigrations` -> `python manage.py migrate`
  * создать суперпользователя `python manage.py createsuperuser`
  * зайти на `<основная ссылка>/admin`, ввести user и password

# 2. Блог (blog app)