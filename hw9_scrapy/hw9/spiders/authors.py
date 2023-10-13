import asyncio
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.item import Item, Field

class AuthorItem(Item):
    fullname = Field()
    born_date= Field()
    born_location= Field()
    description= Field()
    
class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    
    async def parse(self, response, **args):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield response.follow(url=self.start_urls[0] + quote.xpath('span/a/@href').get(), callback=self.nested_parse_author)
            
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        
        if next_link:
             yield scrapy.Request(url=self.start_urls[0] + next_link)

    async def nested_parse_author(self, response):
        author = response.xpath('/html//div[@class="author-details"]')
        fullname = author.xpath("h3[@class='author-title']/text()").get().strip(),
        born_date = author.xpath("p/span[@class='author-born-date']/text()").get().strip(),
        born_location = author.xpath("p/span[@class='author-born-location']/text()").get().strip()[3:],
        description = author.xpath("div[@class='author-description']/text()").get().strip()
        yield AuthorItem(fullname=fullname, born_date=born_date, born_location=born_location, description=description)

async def main_authors():
    process = CrawlerProcess()
    process.crawl(AuthorsSpider)
    process.start()
    process.join()
    
if __name__ == '__main__':
    asyncio.run(main_authors())
