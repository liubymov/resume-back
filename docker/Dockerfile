FROM python:3.6-slim


COPY ./docker/entrypoint.sh /entrypoint.sh
COPY ./requirements.txt /usr/src/resume/requirements.txt

RUN \
       chmod +x /entrypoint.sh \
    && pip install -r /usr/src/resume/requirements.txt

COPY . /usr/src/resume

WORKDIR /usr/src/resume

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
