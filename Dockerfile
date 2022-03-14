FROM python:3.7.12-slim-buster

LABEL application=canyon-notifier

COPY * ./

RUN apt-get update && \
    pip install --requirement requirements.txt && \
    python setup.py install

CMD ["canyon-notifier"]
