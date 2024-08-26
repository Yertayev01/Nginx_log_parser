ADMIN PAGE:
username: admin
email: admin@mail.com
password: admin

# Django Nginx Log Aggregator

## Overview

This Django application is designed to parse and aggregate Nginx log files. The application includes a Django management command for parsing log files, a model for storing parsed data, and views for displaying data through Django Admin and Django REST Framework (DRF).

## Features

- **Management Command:** Parses Nginx log files and stores data in the database.
- **Model:** Represents log data with fields for IP address, date, HTTP method, request URI, response code, and response size.
- **Django Admin Interface:** Provides an interface for managing and viewing parsed log data.
- **DRF API:** Exposes data through an API with pagination, filters, and search capabilities, and includes Swagger for API documentation.
- **Docker Support:** Docker and Docker Compose configuration for easy deployment.
- **Testing:** Unit tests for validation and correctness.

## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose (for Docker setup)
- PostgreSQL (or another supported database)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yertayev01/Nginx_log_parser.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Configure your database settings in `nginx_log/settings.py`.
    - Run the following commands to apply migrations:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Management Command Usage

To parse and import a log file into the database, use the following command:

```bash
python manage.py import_logs https://drive.google.com/uc?id=18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp

## Docker Setup

1. Build the Docker Image:
 
docker-compose build

2. Run the Docker container:

docker-compose up

3. Management Command Usage:

docker-compose exec web python manage.py parse_log "https://drive.google.com/uc?export=download&id=18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp"

## API Documentation

http://localhost:8081/swagger/

# Testing

python manage.py test