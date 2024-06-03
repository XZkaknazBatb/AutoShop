Установка
Шаг 1. Создайте виртуальное окружение
python -m venv venv
Шаг 2. Активируйте виртуальное окружение
venv\Scripts\activate
Шаг 3. Установите зависимости
pip install -r requirements.txt
Шаг 4. Замените уникальный ключ в файле .env (находится в корне проекта)
Шаг 5. Запустите миграции и загрузите данные в БД
cd onlineFeedStore
python manage.py migrate
python manage.py loaddata ../fixtures/goods/categories.json
python manage.py loaddata ../fixtures/goods/products.json
Шаг 6. Запустите сервер
python manage.py runserver
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/admin/. Введите имя пользователя и пароль администратора, чтобы войти в панель управления магазином.


ИМЯ ПОЛЬЗОВАТЕЛЯ: Семён
ПАРОЛЬ АДМИНИСТРАТОРА: 1qaz2wsx3edC_