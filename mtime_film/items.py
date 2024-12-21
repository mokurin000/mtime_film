# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# ========================================= #
#                时光网实体类
# ========================================= #


class MtimeMovieInfoItem(scrapy.Item):
    """时光网电影基本信息类"""

    movie_id = scrapy.Field()
    movie_url = scrapy.Field()
    movie_name = scrapy.Field()
    country = scrapy.Field()
    movie_types = scrapy.Field()
    date = scrapy.Field()
    length = scrapy.Field()
    rating = scrapy.Field()
