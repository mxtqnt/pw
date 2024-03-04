FROM python:3.8-alpine

RUN apk add --update \
    rust cargo build-base libffi-dev openssl-dev \
    xmlsec xmlsec-dev \
  && rm -rf /var/cache/apk/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY web /app

EXPOSE 8000
CMD ["python", "/app/index.py"]
