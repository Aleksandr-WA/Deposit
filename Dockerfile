# Используем официальный Python образ как базовый
FROM python:3.12.5-slim

# Устанавливаем Poetry
RUN pip install poetry

# Создаем рабочую директорию для приложения
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта с помощью Poetry
RUN poetry install --no-root --only main

# Копируем оставшиеся файлы проекта
COPY . .

# Установите переменную окружения
ENV PYTHONUNBUFFERED=1

WORKDIR deposit
