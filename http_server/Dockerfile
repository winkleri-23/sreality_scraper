FROM python:3.9
WORKDIR /usr/src/http_server
COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

COPY . .
RUN touch srealityFlats.html
CMD ["python", "server.py"]