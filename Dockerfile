FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./app /app
COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

