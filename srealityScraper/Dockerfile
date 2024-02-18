FROM python:latest
WORKDIR /usr/src/srealityScraper
COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --upgrade pip
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt


COPY . .
CMD ["scrapy", "crawl", "sreality"]