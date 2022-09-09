ARG DOCKER_REGISTRY

FROM ${DOCKER_REGISTRY}python:3.8.13-alpine3.16

# copy project
COPY . ./whiteapp

EXPOSE 8000

# install dependencies
RUN apk --update add --no-cache libpq-dev gcc gfortran build-base wget libpng-dev openblas-dev linux-headers \
&& pip install --upgrade pip \
&& pip install pipenv \
&& chown -R postgres whiteapp \
&& cd whiteapp \
&& pipenv install --system --deploy \
&& python manage.py collectstatic --noinput \
&& python manage.py makemigrations

USER postgres

WORKDIR whiteapp

ENTRYPOINT psql -h ${POSTGRES_URL} -p ${POSTGRES_PORT} -U ${POSTGRES_MASTER_USER} -d ${POSTGRES_MASTER_DB} -tc "CREATE SCHEMA IF NOT EXISTS ${POSTGRES_SCHEMA}" \
&& python manage.py migrate \
&& python manage.py ensuresuperuser --password=${PASSWORD} --username=${USERNAME} --email=Groupe-recherche-operationnelle.GRO@credit-agricole-sa.fr \
&& gunicorn DjangoSite.wsgi:application --bind 0.0.0.0:8000 --worker-class=gevent
