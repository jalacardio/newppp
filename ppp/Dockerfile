FROM python:3.8.2
LABEL maintainer leonardy
ENV PYTHONUNBUFFERED 1
RUN mkdir /pxp_src
WORKDIR /pxp_src
COPY requirements.txt /pxp_src/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
COPY . /pxp_src/
