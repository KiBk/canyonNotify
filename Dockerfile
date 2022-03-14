FROM python:3.7.12-slim-buster

LABEL application=canyon-notifier

WORKDIR /app

COPY canyon_notifier ./canyon_notifier
COPY requirements.txt ./
COPY setup.py ./

RUN apt-get update && \
    pip install --requirement requirements.txt && \
    python setup.py install

CMD ["canyon-notifier"]
