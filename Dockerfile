FROM python:3.9

RUN mkdir /opt/tmRandom

COPY tmRandom /opt/tmRandom

ADD wsgi.py /opt

ADD requirements.txt /

RUN pip3 install -r /requirements.txt

WORKDIR /opt

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0 wsgi:app
