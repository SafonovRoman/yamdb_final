# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.9

ENV LANG=C.UTF-8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

CMD python manage.py migrate

CMD python manage.py collectstatic