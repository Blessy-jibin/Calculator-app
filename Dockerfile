FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN python setup.py develop