<h1 align="center">Сервис уведомлений</h1>

### При создании проекта использовался следующий стек технологий:
- Django framework.
- Django REST framework.
- Sqlite database.
- Celery.
- Redis.
- Swagger.

### Для запуска проекта нужно:
- Запустить Redis в Docker.
```
sudo docker run -d -p 6379:6379 redis
```
- Клонировать репозиторий "fabriqe".
- создать виртуальное окружение в папке с проектом:
```
python3 -m venv .venv
```
- Активировать виртуальное акружение:
```
source .venv/bin/activate
```
- Установить зависимости:
```
pip install -r requirements.txt
```
- Запустить сервер:
```
./manage.py runserver
```
- В другом окне терминала запустить celery worker:
```
celery -A mailing_list worker -l info
```
- В еще одном окне терминала запустить celery beat:
```
celery -A mailing_list beat -l info
```
### API для работы с сервисом:
- Получение общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам:
```
(GET)/mailings/general_statistics/
```
- Получение детальной статистики отправленных сообщений по конкретной рассылке:
```
(GET)/mailings/{id}/detail_statistics/
```
- Добавление новой рассылки со всеми её атрибутами:
```
(POST)/mailings/
```
- Обновление атрибутов рассылки:
```
(PUT)/mailings/{id}/
```
- Обновление атрибутов рассылки:
```
(PATCH)/mailings/{id}/
```
- Удаление рассылки:
```
(DELETE)/mailings/{id}/
```
- Добавление нового клиента в справочник со всеми его атрибутами:
```
(GET)/clients/
```
- Обновление данных атрибутов клиента:
```
(PUT)/clients/{id}/
```
- Обновление данных атрибутов клиента:
```
(PATCH)/clients/{id}/
```
- Удаление клиента:
```
(DELETE)/clients/{id}/
```

### Были выполнены дополнительные задания
5. Сделать так, чтобы по адресу */docs/* открывалась страница со Swagger UI и в нём отображалось описание разработанного API.
8. Реализовать дополнительный сервис, который раз в сутки отправляет статистику по обработанным рассылкам на email
9. Удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.


