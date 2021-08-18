# pull official base image
FROM docker-remote.registry.saas.cagip.group.gca/library/python:3.8-slim

ARG SECRET_KEY
ARG NAME
ARG USER_DB
ARG HOST
ARG PORT
ARG TEST_DB
ARG TEST_STATIC

ENV SECRET_KEY ${SECRET_KEY}
ENV NAME ${NAME}
ENV USER_DB ${USER_DB}
ENV PASSWORD ${PASSWORD}
ENV HOST ${HOST}
ENV PORT ${PORT}
ENV TEST_DB ${TEST_DB}
ENV TEST_STATIC ${TEST_STATIC}

# copy project
COPY . .

EXPOSE ${PORT}

# install dependencies
RUN apt update && apt install -y libpq-dev
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install
RUN pipenv run python manage.py collectstatic --noinput
RUN pipenv run python manage.py makemigrations
CMD pipenv run python manage.py migrate && pipenv run python manage.py ensure_superuser --password=${PASSWORD} --username=${USER_DB} --email=Groupe-recherche-operationnelle.GRO@credit-agricole-sa.fr && pipenv run gunicorn DjangoSite.wsgi:application --bind ${HOST}:${PORT}
