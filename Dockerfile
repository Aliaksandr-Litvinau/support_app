FROM python:3.10

WORKDIR /support_app
COPY . .

RUN apt-get update && \
    apt-get upgrade

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install -U pip poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/support_app/docker-entrypoint.sh", "python", "django"]




