# Base image
FROM python:3.12-bullseye as base

RUN apt update
RUN apt install gettext -y

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Install Poetry
RUN pip install poetry

# Copy project files needed for dependency installation
COPY pyproject.toml poetry.lock .

FROM base as development

RUN poetry install --no-root

RUN poetry run playwright install --with-deps

# Copy the rest of the application code
COPY . .

# Change file permission to executable
RUN chmod 755 /code/start-django.sh

# Expose port and set the command (update as needed for your project)
EXPOSE 8000
CMD ["/code/start-django.sh"]

FROM base as production

RUN poetry install --only-main --no-root

# Copy the rest of the application code
COPY . .

# Change file permission to executable
RUN chmod 755 /code/start-django.sh

# Expose port and set the command (update as needed for your project)
EXPOSE 8000
CMD ["/code/start-django.sh"]