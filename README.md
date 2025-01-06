# Requirements

## Install pyenv

```
brew install pyenv
pyenv version
pyenv install -l
pyenv global 3.12.2
```

## Install pipx

```
brew install pipx
pipx ensurepath
```

## Install `poetry`

Dependencies and packages manager for python

```
pip install poetry
poetry new djangoapp
poetry install
```

verify installation:

```
poetry run django-admin --version
5.0.3
```

# Starting the Project

```
poetry run django-admin startproject djangoapp .
```

## start application

```
poetry run python manage.py runserver
```

## Run Migration

```
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

## Create an `app`

```
poetry run python manage.py startapp app
```
