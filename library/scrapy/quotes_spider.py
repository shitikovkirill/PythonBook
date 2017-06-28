import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import cmdline


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# if __name__ == "__main__":
#
#     process = CrawlerProcess({
#         'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#     })
#
#     process.crawl(QuotesSpider)
#     process.start() # the script will block here until the crawling is finished
#
#     cmdline.execute("scrapy crawl myspider".split())
