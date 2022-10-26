# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./app /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]