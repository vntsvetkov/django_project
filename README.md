Проект на фреймворке Django

Выгрузите репозиторий командой git clone https://github.com/vntsvetkov/django.git

Убедитесь, что у вас установлен python 3.12

В этом репозитории уже есть виртуальное окружение на версии python 3.12

Запустите проект командой python manage.py runserver

Если django server не стартует сразу, то активируйте venv

.venv\Scripts\activate или venv\Scripts\activate

Запустите еще раз проект командой python manage.py runserver

Перейдите по адресу http://127.0.0.1:8000 - стартовая страница


Полезные команды:

Для создания виртуального окружения выполните python -m venv venv

Установка Django в активированое окружение pip install django

Создание проекта django-admin startproject myproject . (точка в конце важна)

Создание приложения в проекте python manage.py startapp myapp (или другое нахвание)
