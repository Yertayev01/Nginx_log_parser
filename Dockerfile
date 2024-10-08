# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]