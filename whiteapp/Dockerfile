# pull official base image
FROM docker-remote.registry.saas.cagip.group.gca/library/python:3.8-slim

ARG SECRET_KEY
ARG APP_USER
ARG PASSWORD
ARG TEST_DB
ARG TEST_STATIC

ENV SECRET_KEY ${SECRET_KEY}
ENV APP_USER ${APP_USER}
ENV PASSWORD ${PASSWORD}
ENV TEST_DB ${TEST_DB}
ENV TEST_STATIC ${TEST_STATIC}

# copy project
COPY . .

EXPOSE 8000

# install dependencies
RUN apt update \
&& apt install -y libpq-dev gcc \
&& pip install --upgrade pip \
&& pip install pipenv \
&& pipenv install \
&& pipenv run python manage.py collectstatic --noinput \
&& pipenv run python manage.py makemigrations

CMD pipenv run python manage.py migrate && pipenv run python manage.py ensure_superuser --password=${PASSWORD} --username=${APP_USER} --email=Groupe-recherche-operationnelle.GRO@credit-agricole-sa.fr && pipenv run gunicorn DjangoSite.wsgi:application --bind 0.0.0.0:8000
