import scrapy 
from datetime import datetime
from linkedin_job.items import JobItem

file_postfix = datetime.now().strftime('%Y%m%d')

class linkedin_job(scrapy.Spider):
    name = 'linkedin_job'
    custom_settings = {'FEEDS' : { f'job_data_{file_postfix}.csv': { 'format': 'csv'}}}
    
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=3836773060&geoId=104195383&keywords=data%20engineer&location=Vietnam&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&start='
    
    def start_requests(self):
       job_on_page = 0
       start_url = self.url + str(job_on_page)
       yield scrapy.Request(url = start_url, callback=self.parse, meta={'job_on_page': job_on_page})

    def parse(self, response):
        job_on_page = response.meta['job_on_page']

        jobs = response.css('li')

        job_num = len(jobs)

        for job in jobs:
            job_item = JobItem()
            
            job_item['job_url'] = job.css('a::attr(href))').get(default='not-found').strip()
            
            yield job_item

        if job_num > 0:
            job_on_page = int(job_on_page) + 25
            next_url = self.url + str(job_on_page)
            
            yield scrapy.Request(url = next_url, callback= self.parse, meta={'job_on_page': job_on_page}) 