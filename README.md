# Welcome to GitHub Desktop!

# Quotes Scraper

This project is a simple web scraping exercise using 
Scrapy. It scrapes quotes, authors, and tags from [Quotes 
to Scrape](http://quotes.toscrape.com).

## Project Description

This Python script is designed to scrape data from a 
website as a practice in web scraping. It uses the Scrapy 
framework to extract quotes, their authors, and associated 
tags from a webpage and print them to the console. This is 
a basic example to demonstrate the capabilities of Scrapy 
and how it can be used for web data extraction.

## Prerequisites

Before you can run this project, ensure you have the 
following installed:

- Python 3.6+
- Scrapy
- nest_asyncio

You can install the required Python packages using pip:


pip install scrapy nest_asyncio


## How to Run

1. Clone the repository to your local machine:
    git clone 
https://github.com/yourusername/quotes-scraper.git

2. Navigate to the project directory:
    cd quotes-scraper

3. Run the spider using the following command:
    python quotes_spider.py

   This will start the Scrapy spider, and it will begin to 
scrape the data from the website. The extracted data will 
be printed to the console.

## Code Overview

    QuotesSpider Class : The core of this project, where 
the scraping logic is implemented. It starts from the 
provided URL and parses the HTML content to extract the 
desired information.

    parse Method : This method processes the HTML response 
from the website, extracting the quotes, authors, and tags, 
then printing them out.

## Acknowledgments

    This project is for educational purposes and to 
practice web scraping using Scrapy.
    Data is scraped from the [Quotes to 
Scrape](http://quotes.toscrape.com) website.


