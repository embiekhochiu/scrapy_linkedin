import scrapy

class linkedin_jobItem(scrapy.Item):
    job_title = scrapy.Field()
    job_url = scrapy.Field()
    job_location = scrapy.Field()
    job_company = scrapy.Field()