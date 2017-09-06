FROM jupyter/datascience-notebook
COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

USER root

# Add demo app
COPY ./app /app
WORKDIR /app