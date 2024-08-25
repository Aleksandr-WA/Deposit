# Используем официальный Python образ как базовый
FROM python:3.12.5-slim

# Установка PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Устанавливаем Poetry
RUN pip install poetry

# Создаем рабочую директорию для приложения
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости проекта с помощью Poetry
RUN poetry install --no-dev

# Копируем оставшиеся файлы проекта
COPY . /app/

# Установите переменную окружения
ENV PYTHONUNBUFFERED=1
