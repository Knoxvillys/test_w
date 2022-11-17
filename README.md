Проект для **Фабрики решений** на **Python-разработчик (Django, DRF)**

**Порядок установки:**

Клонировать репозиторий к себе, установить и активировать виртуальное окружение:

    git clone git@github.com:Knoxvillys/test_w.git
    python -m venv venv
    venv\Scripts\activate.bat 
    
перейти в папку проекта, установить зависимости:

    cd test_w
    pip install -r requirements.txt
    
запустить и применить миграции:

    python manage.py makemigrations
    python manage.py migrate
    
Запустить проект:

    python manage.py runserver
   
