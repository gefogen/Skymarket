## CW06. Skymarket - рекламный сайт, похожий на авито

### Реализация

1. Бэкенд: django restframework
2. База данных: postgresql
3. Backend-сервер: gunicorn
4. Веб-сервер: nginx (из образа докера)
5. Фронтенд: react (было предоставлено)

интерфейс доступен по адресу: localhost:3000
серверная часть по адресу: localhost:8000

### Для запуска проекта локально, используя докер для каждого сервиса

Проект настроен на запуск всех необходимых контейнеров докеров и заполнение базы данных с помощью одной команды.
Просто выполните следующую команду: `docker compose up --build -d`


PS Если вы не видите frontend часть, просто отключите блокировщик рекламы.... 