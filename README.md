# Image Determinator

Сервис для классификации изображений: пользователи загружают картинку и получают информацию о том, что на ней изображено.

## Установка и запуск

1. Склонируйте репозиторий на ваш компьютер:
    ```
    git clone https://github.com/warmsnow17/image_determinator.git
    ```
2. Перейдите в директорию проекта:
    ```
    cd image_determinator
    ```
3. Установите все необходимые зависимости с помощью [Poetry](https://python-poetry.org/):
    ```
    poetry install
    ```
4. Примените миграции к базе данных:
    ```
    python manage.py migrate
    ```
5. Запустите сервер разработки Django:
    ```
    python manage.py runserver
    ```
    
## Использование

1. Откройте в браузере [http://127.0.0.1:8000/upload_image/](http://127.0.0.1:8000/upload_image/).
2. Загрузите изображение.
3. Нажмите "Показать результат" для классификации изображения.

## Запуск тестов

Запустите тесты следующей командой:

python manage.py test app

![Рабочая панель](https://github.com/warmsnow17/image_determinator/media/images/picture.png)
