from scrapy.spiders import Spider
from first.items import Doubanmovieitem

class DoubanSpider(Spider):
    name ='douban_movie_top250'
    start_urls =['https://movie.douban.com/top250']

    def parse(self, response):
        item = Doubanmovieitem()
        movies =response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking']= movie.xpath('.//div[@class="pic"]/em/text()').extract[0]
            item['movie_name'] =movie.xpath('.//div[@class="hd"]/span[1]/text()').extract[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract[0]
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item
