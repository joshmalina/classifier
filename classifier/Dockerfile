FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app app
COPY glove.6B.50d.txt /data/glove
COPY model.pkl /models/model.pkl

COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt