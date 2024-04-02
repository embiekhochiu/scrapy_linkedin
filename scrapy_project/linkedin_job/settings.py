BOT_NAME = 'linkedin_job'

SPIDER_MODULES = ['linkedin_job.spiders']
NEWSPIDER_MODULE = 'linkedin_job.spiders'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'linkedin_job.middlewares.RotateUserAgentMiddleware': 400, 
}

CONCURRENT_REQUESTS_PER_DOMAIN = 1

DOWNLOAD_DELAY = 3