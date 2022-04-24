# Интеграция базового образа
FROM python:3.8

# Назначаю рабочий каталог внутри контейнера
# Каталог будет создан если его не было
# В дальнейшем будет использоваться как базовый
WORKDIR /tests

# Копирую файл с зависимостями
COPY requirements.txt .

# Устанавливаю менеджер пакетов и необходимые библиотеки
RUN pip install -r requirements.txt

# Копирую остальные файлы проекта
#COPY tests/page_objets .
COPY tests .
#COPY tests/conftest.py .
#
#COPY tests/local_opencard .
#COPY tests/drivers .
#COPY tests/common .

EXPOSE 4444

RUN docker run -d --name selenoid -p 4444:4444 aerokube/selenoid:latest-release

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
CMD ["pytest", "--executor", "chrome"]
