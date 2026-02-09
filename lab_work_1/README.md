# Лабораторная работа 1

## Структура проекта
```
/lab_work_1
├── /docs
├── /src
|   ├── /app
|   |   ├── main_window.py      - Интерфейс приложения
|   |   └── main_window.ui      - Интерфейс приложения
|   ├── /data
|   |   └── weatherHistory.csv  - Набор данных для анализа
|   ├── /img
|   ├── /pipeline
|   |   ├── lr_model_1.pickle   - Сохраненная модель (влажность, температура)
|   |   ├── lr_model_2.pickle   - Сохраненная модель (влажность, температура, скорость ветра)
|   |   ├── models.py           - Имплементация моделей
|   |   ├── scaler_1.pickle     - Сохраненный 
|   |   └── scaler_2.pickle     - Сохраненный 
|   ├── .gitignore
|   ├── main.py                 - Демонстрационное приложение
|   ├── requirements.txt        - Список зависимостей
|   └── weather.ipynb           - Анализ данных и построение моделей
└── README.md                   - Вы здесь
```

## Запуск приложения
1. Перейти в дирректорию `\src`
```bash
cd .../src
```
2. Создать виртуальное окружение:
```bash
python -m venv venv
```
3. Активировать виртуальное окружение:
```bash
source venv/Scripts/activate
```
4. Установить зависимости:
```bash
pip install -r requirements.txt
```
5. Запустить приложение:
```bash
python main.py
```
## Демонстрация приложения
![Здесь показан интерфейс приложения](/lab_work_1/src/img/image.png)

## При правках в интерфейс .ui сконвертируйте .py
```bash
python -m PyQt5.uic.pyuic app/main_window.ui -o app/main_window.py
```