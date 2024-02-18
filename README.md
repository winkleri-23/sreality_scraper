# sreality scraper 

This task was implemented as a part of the recruitment process for the position of Python Developer.

## Assignment: 
Use Scrapy framework to scrape the first 500 items (title, image URL) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in Python and show these 500 items on a simple page (title and image) and put everything to a single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Solution:
The solution consists of three parts: 
1. Scrapy spider that scrapes the first 500 items from the sreality.cz website and saves them to the Postgresql database
2. Simple HTTP server that retrieves the scraped items from the database and displays them on a simple page
3. Postgresql database to store the scraped items

The solution is dockerized and can be run with a single command `docker-compose up` in the root directory of the project. The scraped items can be viewed on the http://127..0.0.1:8080 page as requested in the assignment.

## Directory structure

The project is organized as follows:
```
.
├── README.md
├── compose.yaml
├── http_server
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── server.py
└── srealityScraper
    ├── Dockerfile
    ├── requirements.txt
    ├── scrapy.cfg
    └── srealityScraper
```

- `compose.yaml` - docker-compose file that defines the services to be run
- `http_server` - directory containing the simple HTTP server
- `srealityScraper` - directory containing the Scrapy spider
    - important files:
        - `Dockerfile` - Dockerfile for the Scrapy spider
        - `srealityScraper/spiders/flat.py` - Scrapy spider that scrapes the sreality.cz website
        - `srealityScraper/pipeline.py` - Scrapy pipeline that saves the scraped items to the Postgresql database
## Sources
- Scrapy documentation: https://docs.scrapy.org/en/latest/
- Sreality Rest API documentation: https://dspace.cvut.cz/bitstream/handle/10467/103384/F8-BP-2021-Malach-Ondrej-thesis.pdf?sequence=-1&isAllowed=y