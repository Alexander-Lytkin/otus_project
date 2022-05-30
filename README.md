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

# Selenoid запуск/остановка

```bash
выполнить {binary_name} selenoid start/stop
```

# Генерация отчетов allure 

```bash
выполнить находясь в директории с тестами, генерация отчета и открытие его в html странице
allure generate -c && allure open
```


# Запуск jenkins

```
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```