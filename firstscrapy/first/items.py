# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovieitem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 人数
    score_num = scrapy.Field()
    # 图片路径
    #pic_link = scrapy.Field()
    # 简介
    movie_intro = scrapy.Field()
    #导演
    movie_direct = scrapy.Field()