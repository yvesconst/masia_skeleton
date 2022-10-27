# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat
WORKDIR /usr/src/app
COPY ./app /usr/src/app
RUN pip install -r requirements.txt
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]