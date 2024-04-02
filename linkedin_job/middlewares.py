from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random


class RotateUserAgentMiddleware(UserAgentMiddleware):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/76.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        try:
            request.headers.setdefault('User-Agent', random.choice(self.user_agents))
        except IndexError:
            pass