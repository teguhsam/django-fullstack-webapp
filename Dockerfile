# Base image
FROM python:3.12-bullseye

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Install Poetry
RUN pip install poetry

# Copy project files needed for dependency installation
COPY pyproject.toml poetry.lock .

# Install dependencies (using --no-root if you don't want to install the current project)
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Expose port and set the command (update as needed for your project)
EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
