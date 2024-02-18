FROM python:3.9
WORKDIR /usr/src/sreality/http_server

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip

COPY . .
CMD ["python3", "server.py"]

