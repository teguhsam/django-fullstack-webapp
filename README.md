# DjangoApp Project

## Requirements

### Install pyenv

`pyenv` is used to manage different versions of Python.

```bash
brew install pyenv
pyenv version
pyenv install -l
pyenv global 3.12.2
```

### Install pipx

## Install pipx

`pipx` is used to install and manage Python applications in isolated environments.

```
brew install pipx
pipx ensurepath
```

### Install `poetry`

Poetry is a dependency and package manager for Python.

```
pip install poetry
poetry new djangoapp
poetry install
```

Verify installation:

```
poetry run django-admin --version
# Example output: 5.0.3
```

# Starting the Project

1. Create a new Django project:

   ```
   poetry run django-admin startproject djangoapp .
   ```

2. start application

   ```
   poetry run python manage.py runserver
   ```

3. Run Migration

   ```
   poetry run python manage.py showmigrations

   poetry run python manage.py migrate
   ```

4. Create a superuser
   ```
   poetry run python manage.py createsuperuser
   ```

## Create an `app`

```
poetry run python manage.py startapp app
```

# Processes

## Make Migrations

1. Create migrations:

   ```
   poetry run python manage.py makemigrations
   ```

2. Apply migrations:
   ```
   poetry run python manage.py migrate
   ```

## Run the app

```
poetry run python manage.py runserver
```

# Docker

Build docker

```
docker build -t djangoapp .
```

Run container:

```
docker run -p 8005:8000 --name djangoapp djangoapp

docker run -p 8005:8000 --name djangoapp -v "$(pwd):/code" djangoapp
```

Run Migration:

```
docker exec djangoapp poetry run python manage.py migrate
```

Prune:

```
docker builder prune -a
```

# Tailwind

```
npx tailwindcss -i ./static/input.css -o ./static/output.css --watch
```
