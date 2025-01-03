﻿FROM python:3.11
WORKDIR /app
COPY ./app
RUN pip install gmqtt
CMD [python mqtt_listener.py]
RUN pip install --timeout=120 --retries=10 gmqtt
