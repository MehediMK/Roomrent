# Roomrent Project Using Django Framework

## Prerequisites
  - Python 3.8+
  - Postgres
  - Virtualenv and Pip

## For development
  - create a virtual env `pip virtualenv env`
  - For activate env write on you terminal `source env/bin/activate` (*linux) on `env\Scripts\activate` (Windows)
  - Install packages `pip install -r requirements.txt`
  - To configure your Postgres database and secret_key change file name from `config.py sample` to `config.py` change connections accordingly. which is given main project app directory.
  - run on your terminal `python manage.py migrate`
  - run `python manage.py runserver`

## Helpful commands
  - `python manage.py makemigrations` "for migration"
  - `python manage.py runserver host:port` "for starting dev. server"
  - `python manage.py startapp app_name` "for new app"
  - `python manage.py createsuperuser` "for create superuser"


