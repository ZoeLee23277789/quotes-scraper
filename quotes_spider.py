# Import necessary modules
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging

# Configure IPython to support asynchronous operations
import nest_asyncio
nest_asyncio.apply()

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('span small::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            
            yield {
                'text': text,
                'author': author,
                'tags': tags,
            }
            
            print("Text: {}\nAuthor: {}\nTags: {}\n".format(
                text, 
                author, 
                tags
            ))
# Configure Scrapy logging
configure_logging()

# Create and start the Scrapy crawler process
process = CrawlerProcess(Settings())
process.crawl(QuotesSpider)
process.start()