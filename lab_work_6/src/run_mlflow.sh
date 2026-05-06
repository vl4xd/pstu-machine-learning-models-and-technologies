#!/bin/bash
# Запуск MLflow сервера с хранением в папках проекта

# Определяем директорию, в которой лежит этот скрипт
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Создаём папки
mkdir -p mlflow/mlruns mlflow/mlartifacts

# Запускаем сервер (использует виртуальное окружение проекта)
mlflow server \
    --backend-store-uri "./mlflow/mlruns" \
    --default-artifact-root "./mlflow/mlartifacts" \
    --host localhost \
    --port 5000