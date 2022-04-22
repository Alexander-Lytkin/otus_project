# Перед запуском проекта выполнить в командной строке: 

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

# Работа с докером

```bash
 docker-compose up -d - запуск контейнера в фоне
 docker ps - посмотреть количество запущенных контейнеров
 docker kill {id контейнера} - убить\остановить контейнер
 docker system prune - удалить все не используемые контейнеры
```

# Локальный IP адрес для запуска тестов в контейнере

```bash
 pytest test_example.py --url http://127.0.1.0/
```

# Задание 9
Необходимо выполнить скрипт
По умолчанию уже используется путь файла для лога "/home/al/PycharmProjects/OTUS/otus_project/nine_homework/logs/"
```bash
 python3 log_reader.py 
 
 Чтение логов в дириктории
(venv) al@al:~/PycharmProjects/OTUS/otus_project/nine_homework$ python3 log_reader.py -path logs/
{'Отчёт': [{'Общее количество выполненных запросов': '3216723', 'Количество запросов по HTTP-методам': "{'GET': '2247849', 'HEAD': '49971', 'POST': '921431', 'PUT': '70', 'DELETE': '2', 'CONNECT': '0', 'OPTIONS': '39', 'TRACE': '0', 'PATCH': '0'}", 'Топ 3 IP адресов': "['193.106.31.130', '198.50.156.189', '5.112.235.245']", 'Топ 3 самых долгих запросов': '[\'100.1.14.108 - - [22/Sep/2019:23:04:20 +0200] "HEAD /wp-admin/admin-ajax.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:01:49:08 +0200] "HEAD /templates/arc/artx.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:18:42:51 +0200] "GET /templates/system/404.php HTTP/1.1" 404 230 "-" "Python/3.7 aiohttp/3.6.1" 10000\\n\']'}]}
{'Отчёт': [{'Общее количество выполненных запросов': '269', 'Количество запросов по HTTP-методам': "{'GET': '266', 'HEAD': '0', 'POST': '3', 'PUT': '0', 'DELETE': '0', 'CONNECT': '0', 'OPTIONS': '0', 'TRACE': '0', 'PATCH': '0'}", 'Топ 3 IP адресов': "['193.106.31.130', '198.50.156.189', '5.112.235.245']", 'Топ 3 самых долгих запросов': '[\'100.1.14.108 - - [22/Sep/2019:23:04:20 +0200] "HEAD /wp-admin/admin-ajax.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:01:49:08 +0200] "HEAD /templates/arc/artx.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:18:42:51 +0200] "GET /templates/system/404.php HTTP/1.1" 404 230 "-" "Python/3.7 aiohttp/3.6.1" 10000\\n\']'}]}
(venv) al@al:~/PycharmProjects/OTUS/otus_project/nine_homework$ 

Чтение файла
(venv) al@al:~/PycharmProjects/OTUS/otus_project/nine_homework$ python3 log_reader.py -path /home/al/PycharmProjects/OTUS/otus_project/nine_homework/logs/access.log
{'Отчёт': [{'Общее количество выполненных запросов': '3216723', 'Количество запросов по HTTP-методам': "{'GET': '2247849', 'HEAD': '49971', 'POST': '921431', 'PUT': '70', 'DELETE': '2', 'CONNECT': '0', 'OPTIONS': '39', 'TRACE': '0', 'PATCH': '0'}", 'Топ 3 IP адресов': "['193.106.31.130', '198.50.156.189', '5.112.235.245']", 'Топ 3 самых долгих запросов': '[\'100.1.14.108 - - [22/Sep/2019:23:04:20 +0200] "HEAD /wp-admin/admin-ajax.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:01:49:08 +0200] "HEAD /templates/arc/artx.php HTTP/1.1" 404 0 "-" "python-requests/2.22.0" 10000\\n\', \'100.1.14.108 - - [23/Sep/2019:18:42:51 +0200] "GET /templates/system/404.php HTTP/1.1" 404 230 "-" "Python/3.7 aiohttp/3.6.1" 10000\\n\']'}]}
(venv) al@al:~/PycharmProjects/OTUS/otus_project/nine_homework$ 

```
