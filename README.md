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