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
 python3 readlog.py 
 python3 readlog.py -path "/home/al/PycharmProjects/OTUS/otus_project/nine_homework/logs/"
```
