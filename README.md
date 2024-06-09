# Тестовое задание для 2ГИС
**Библеотеки:** python, pytest, request, pydantic, pytest-html

## Клонирование репозитория:
```commandline
git clone https://github.com/zomlik/2gis_autotests.git
```
## Создание виртеального окружения:
```commandline
python -m venv venv
./venv/Scripts/activate
```
## Установка зависимостей:
```commandline
pip install -r requirements.txt
```
## Запуск тестов без отчета:
```commandline
pytest
```
## Запуск тестов с генерацией отчета в html:
```commandline
pytest --html=report.html --self-contained-html
```


