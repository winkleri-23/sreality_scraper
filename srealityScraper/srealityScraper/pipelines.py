# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import time


class SrealityscraperPipeline:
    def __init__(self):
        hostname = '127.0.0.1'
        port = '5432'
        username = 'test'
        password = 'test'
        database = 'sreality'

        # Connect to the database
        attempts = 0
        connected = False
        max_attempts = 3
        while not connected and attempts < max_attempts:
            try:
                self.connection = psycopg2.connect(host='database', user=username, password=password, dbname=database, port=port)
                connected = True
            except psycopg2.OperationalError:
                attempts += 1
                print("Failed to connect to the database. Retrying in 5 seconds...")
                time.sleep(3)
        if not connected:
            print("Failed to connect to the database after maximum attempts. Exiting...")
            return

        # handle for exectuing SQL commands
        self.cur = self.connection.cursor()

        # create flat table if not exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flat(
            id serial PRIMARY KEY,
            title text,
            image_urls text
        )
        """)
        
        # delete all records from flat table
        self.cur.execute("""
        DELETE FROM flat *
        """)

    def process_item(self, item, spider):
        ## Define insert statement
        self.cur.execute(""" insert into flat (title, image_urls) values (%s,%s)""", (
            item["title"],
            str(item["image_urls"])
        ))
        ## Execute insert of data into database
        self.connection.commit()

        print('Data inserted into database successfully')
        return item

    def close_spider(self, spider):
        self.connection.close()

