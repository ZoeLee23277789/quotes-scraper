import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
import nest_asyncio

# Configure IPython to support asynchronous operations
nest_asyncio.apply()

class StoresSpider(scrapy.Spider):
    name = "stores"
    start_urls = ['https://www.gyu-kaku.com.tw/store.php']

    custom_settings = {
        'FEEDS': {
            'stores.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
                'fields': None,
                'overwrite': True,
            },
        },
    }

    def parse(self, response):
        store_sections = response.css('div.content-store')
        
        for store_section in store_sections:
            stores = store_section.css('ul li')
            
            for store in stores:
                name = store.css('span::text').get()
                address = store.css('div.text a::text').get()
                phone = None
                
                details = store.css('div.text p::text').getall()
                
                for detail in details:
                    if '電話' in detail:
                        phone = detail.split('：')[1].strip()

                yield {
                    'name': name,
                    'add': address,
                    'phone': phone,
                }

# Configure Scrapy logging
configure_logging()

# Create and start the Scrapy crawler process
process = CrawlerProcess({
    'USER_AGENT': 'Zoe/5.0',
    'LOG_LEVEL': 'INFO',
})
process.crawl(StoresSpider)
process.start()

