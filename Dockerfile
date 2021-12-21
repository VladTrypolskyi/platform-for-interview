FROM python:3.9 - slim

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL 'postrgesql://vlad:1@172.17.0.1:5432/vlad'
ENV FLASK_APP app.py
# COPY requirements.txt requirements.txt
COPY requirements.txt /code/requirements.txt

COPY . /code/

RUN python -m pip install --upgrade pip \
    && apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
    &&pip install -r requirements.txt

EXPOSE 5000
EXPOSE 5432

# CMD psql --host=192.168.64.2/24 --port=5432 --username=vlad -c "SELECT 'SUCCESS !!!';"

# COPY . .
CMD [ "python", "app.py" ]
