FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /forum

COPY requirements.txt /forum/
RUN pip install -r requirements.txt
COPY start.sh /forum/
COPY makinaforum/ /forum/
