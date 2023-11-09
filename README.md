# SHOP_API

### How to install:

python -m venv shop_venv;
source shop_venv/bin/activate or shop_venv\Scripts\activate;
pip install -r requirements;

##### Run migrations:

python manage.py migrate

### How to run application:
python manage.py runserver

##### Create superuser:

python manage.py createsuperuser

### Available commands:

- python manage.py show_urls -  show tab-separated list of (url_pattern, view_function, name) tuples for a project
- python manage.py shell - open django application console
- python manage.py shell_plus --print-sql - open django shell with sql explanation
