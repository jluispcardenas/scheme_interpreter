# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN python3 setup.py install

CMD [ "scheme_interpreter"]
