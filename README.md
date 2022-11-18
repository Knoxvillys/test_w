## Порядок установки
Клонировать репозиторий к себе, установить и активировать виртуальное окружение:
```
    git clone https://github.com/aboronilov/test_task_API_sending
    python -m venv venv
    venv\Scripts\activate.bat 
```
перейти в папку проекта, установить зависимости:
```
    cd test_w
    pip install -r requirements.txt
```

запустить и применить миграции:
```
    python manage.py makemigrations
    python manage.py migrate
```

Запустить проект:

```
    python manage.py runserver
```
