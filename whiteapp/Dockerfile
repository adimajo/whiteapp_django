# pull official base image
FROM python:3.8.3

ARG SECRET_KEY
ARG NAME
ARG USER_DB
ARG HOST
ARG PORT
ARG TEST_DB
ARG TEST_STATIC

ENV the_proxy http://host.docker.internal:3128
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

EXPOSE 8000

# install dependencies
RUN http_proxy=$the_proxy && https_proxy=$the_proxy && apt update && pip install --upgrade pip && pip install pipenv
RUN http_proxy=$the_proxy && https_proxy=$the_proxy && pipenv install
RUN echo $SECRET_KEY
RUN pipenv run python manage.py collectstatic --noinput
RUN pipenv run python manage.py makemigrations
CMD pipenv run python manage.py migrate && pipenv run python manage.py ensure_superuser --password=${PASSWORD} --username=${USER_DB} --email=Groupe-recherche-operationnelle.GRO@credit-agricole-sa.fr && pipenv run gunicorn DjangoSite.wsgi:application --bind 0.0.0.0:8000
