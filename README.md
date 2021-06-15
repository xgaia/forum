# Forum

![CI](https://github.com/xgaia/forum/actions/workflows/django.yml/badge.svg)
[![Docker Build](https://img.shields.io/docker/pulls/xgaia/forum.svg)](https://hub.docker.com/r/xgaia/forum/)

A simple forum, written in python with Django.

## Local install (development)

Clone the repository

```bash
git clone https://github.com/xgaia/forum.git
````

Create and activate a python virtual env

```bash
cd forum
python3 -m venv venv && source venv/bin/activate
````

Install project dependencies

```bash
pip install -r requirements.txt
````

Serve

```bash
python manage.py runserver 8000
````

App is available at [localhost:8000](http://localhost:8000)

## Production deployment with [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/)

Use the `docker-compose.yml` file to deploy the app with docker.
