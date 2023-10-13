import asyncio
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'qoutes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "qoutes.json"}
    
    async def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").get().strip(),
                "quote": quote.xpath("span[@class='text']/text()").get().strip()
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
     
async def main_qoutes():
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
    process.join()
       
if __name__ == '__main__':
   asyncio.run(main_qoutes())     
    