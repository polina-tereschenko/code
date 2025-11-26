# Get started

```shell
python -m venv .venv
python -m pip install django~=4.0.0
source .venv/bin/activate
python manage.py runserver
```

If you edit models.py file do this commands

```shell
python manage.py makemigrations
python manage.py migrate
```

## Run tests

```shell
python manage.py test
```
