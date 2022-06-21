# Куда пойти
Карта Москвы с местами отдыха с подробным описаниям.

### Установка
1. Python3 должен быть уже установлен. 
2. Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
4. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
4. Создайте файл `.env` и пропишите в нем переменные окружения:
- `SECRET_KEY` - [секретный ключ Django](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key);
- `DEBUG` - [флаг включения дебаг-режима](https://docs.djangoproject.com/en/4.0/ref/settings/#debug);
- `ALLOWED_HOSTS` - [список допустимых хостов/доменов](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts).
5. Проведите миграцию командой: 
```python
python manage.py migrate
```
6. Cоздайте суперпользователя командой:
```python
python manage.py createsuperuser
```
### Как запустить
Запустите сервер на локальной машине командой:
```python
python manage.py runserver
```
После чего по адресу http://127.0.0.1:8000/ будет доступен сайт, а по адресу http://127.0.0.1:8000/admin - административная панель.

### Как добавить новое место
В административной панеле, заполнив данные и добавив изображения (можно сортировать их перетаскивая мышью);

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

