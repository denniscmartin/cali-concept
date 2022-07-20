FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY explorer explorer

# Run server with 4 workers and make it external accesible at port 80
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:80", "explorer:create_app()"]