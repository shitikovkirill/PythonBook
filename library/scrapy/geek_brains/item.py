import scrapy

class BrainItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    description = scrapy.Field()
    logo = scrapy.Field()
    teachers = scrapy.Field()