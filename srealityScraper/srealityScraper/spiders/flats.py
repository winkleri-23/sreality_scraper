import scrapy
from srealityScraper.items import FlatItem

class FlatSpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=500']

    def parse(self, response):
        # Parse the JSON response
        jsonresponse = response.json()

        # Iterate over each item in the response
        for item in jsonresponse["_embedded"]['estates']:
            # Send a request to the URL of each item
            yield scrapy.Request('https://www.sreality.cz/api' + item['_links']['self']['href'], callback=self.parse_flat)

    def parse_flat(self, response):
        # Parse the JSON response
        jsonresponse = response.json()

        # Create a new FlatItem object
        flat = FlatItem()

        # Extract the title from the response and assign it to the FlatItem object
        flat['title'] = jsonresponse['name']['value']

        # Extract the image URL from the response and assign it to the FlatItem object
        for images in jsonresponse['_embedded']['images']:
            if images['_links']['dynamicDown']:
                tmp = images['_links']['dynamicDown']['href'].replace('{width}', '400')
                tmp = tmp.replace('{height}', '300')
                flat['image_urls'] = tmp
                break

        # Yield the FlatItem object
        yield flat
