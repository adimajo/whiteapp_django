# pull official base image
FROM docker-remote.registry.saas.cagip.group.gca/library/python:3.8-slim

ARG POSTGRES_MASTER_DB
ARG POSTGRES_MASTER_USER
ARG POSTGRES_MASTER_PASSWORD
ARG POSTGRES_SCHEMA
ARG POSTGRES_PORT
ARG POSTGRES_URL
ARG SECRET_KEY
ARG APP_USER
ARG PASSWORD

ENV POSTGRES_MASTER_DB ${POSTGRES_MASTER_DB}
ENV POSTGRES_MASTER_USER ${POSTGRES_MASTER_USER}
ENV POSTGRES_MASTER_PASSWORD ${POSTGRES_MASTER_PASSWORD}
ENV POSTGRES_SCHEMA ${POSTGRES_SCHEMA}
ENV POSTGRES_PORT ${POSTGRES_PORT}
ENV POSTGRES_URL ${POSTGRES_URL}
ENV PGPASSWORD ${POSTGRES_MASTER_PASSWORD}
ENV SECRET_KEY ${SECRET_KEY}
ENV APP_USER ${APP_USER}
ENV PASSWORD ${PASSWORD}

# copy project
COPY . ./whiteapp

RUN chown nobody:nogroup ./whiteapp

EXPOSE 8000

# install dependencies
RUN apt update \
&& apt install -y libpq-dev gcc \
&& pip install --upgrade pip \
&& pip install pipenv \
&& cd whiteapp \
&& pipenv install --system --deploy \
&& python manage.py collectstatic --noinput \
&& python manage.py makemigrations

USER nobody

ENTRYPOINT su -m postgres -c "psql -h ${POSTGRES_URL} -p ${POSTGRES_PORT} -U ${POSTGRES_MASTER_USER} -d ${POSTGRES_MASTER_DB} -tc \"CREATE SCHEMA IF NOT EXISTS ${POSTGRES_SCHEMA}\"" \
&& python manage.py migrate \
&& python manage.py ensuresuperuser --password=${PASSWORD} --username=${APP_USER} --email=Groupe-recherche-operationnelle.GRO@credit-agricole-sa.fr \
&& gunicorn DjangoSite.wsgi:application --bind 0.0.0.0:8000 --worker-class=gevent
