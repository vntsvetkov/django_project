Проект на фреймворке Django

Выгрузите репозиторий командой git clone https://github.com/vntsvetkov/django.git

В этом репозитории уже есть виртуальное окружение на версии python 3.12, убедитесь, что у вас установлен python 3.12, если нет - установите.

активируйте venv, если он не активировался автоматически

.venv\Scripts\activate или venv\Scripts\activate

Выполнить миграцию БД:
  python manage.py makemigrations
  python manage.py migrate

Запустить скрипты переноса данных в БД

Запустите проект командой python manage.py runserver

Перейдите по адресу http://127.0.0.1:8000 - стартовая страница


Полезные команды:

Для создания виртуального окружения выполните python -m venv venv

Установка Django в активированое окружение pip install django

Создание проекта django-admin startproject myproject . (точка в конце важна)

Создание приложения в проекте python manage.py startapp myapp (или другое нахвание)
