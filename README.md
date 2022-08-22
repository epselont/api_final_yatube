
# API_Yatube

REST API для социальной сети блогеров [Yatube](https://blog-yatube.tk), созданной в рамках учебного курса Яндекс.Практикум

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- система управления версиями - git

## Как запустить проект:

1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/epselont/api_final_yatube
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Выполните миграции:
```
python manage.py migrate
```
4) Создайте суперпользователя:
```
python manage.py createsuperuser
```
5) Запустите сервер:
```
python manage.py runserver
```
____________________________________

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация ([redoc.yaml](https://github.com/epselont/api_final_yatube/tree/master/yatube_api/static)) доступна по адресу http://localhost:8000/redoc/

### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в режиме чтения,
что-либо изменить или создать не получится.
```bash
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
### Примеры работы с API для авторизованных пользователей
Для создания публикации используем:
```bash
POST /api/v1/posts/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Обновление публикации:
```bash
PUT /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
PATCH /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```bash
DEL /api/v1/posts/{id}/
```
Получение доступа к эндпоинту /api/v1/follow/
(подписки) доступен только для авторизованных пользователей.
```bash
GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
- Авторизованные пользователи могут создавать посты,
комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

### Добавить группу в проект нужно через админ панель Django:
```bash
admin/ - после авторизации, переходим в раздел Groups и создаем группы
```
Доступ авторизованным пользователем доступен по JWT-токену (Joser),
который можно получить выполнив POST запрос по адресу:
```bash
POST /api/v1/jwt/create/
```
Передав в body данные пользователя (например в postman):
```bash
{
"username": "string",
"password": "string"
}
```
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
```bash
Authorization: Bearer {your_token}
```
Обновить JWT-токен:
```bash
POST /api/v1/jwt/refresh/ - обновление JWT-токена
```
Проверить JWT-токен:
```bash
POST /api/v1/jwt/verify/ - проверка JWT-токена
```
Так же в проекте API реализована пагинация (LimitOffsetPagination):
```bash
GET /api/v1/posts/?limit=5&offset=0 - пагинация на 5 постов, начиная с первого
```
