# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface

"""
代理配置信息
"""
TUNNEL = "xxx"
USERNAME = "xxx"
PASSWORD = "xxx"
PROXIES = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/"
    % {"user": USERNAME, "pwd": PASSWORD, "proxy": TUNNEL},
    "https": "https://%(user)s:%(pwd)s@%(proxy)s/"
    % {"user": USERNAME, "pwd": PASSWORD, "proxy": TUNNEL},
}


"""
时光网中间件
"""


class MtimeMovieInfoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    """下载中间件

    是一个拦截器，拦截请求和响应

    Returns
    -------
    _type_
        _description_
    """

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """拦截请求"""
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
