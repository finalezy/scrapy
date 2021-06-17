import scrapy
from scrapy.spiders import Spider
from first.items import Doubanmovieitem

class DoubanSpider(Spider):
    name ='douban_movie_top250'
    start_urls =['https://movie.douban.com/top250']

    def parse(self, response):
        item = Doubanmovieitem()
        movies =response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking']= movie.xpath(".//div[@class='pic']/em/text()").extract_first()
            item['movie_name'] =movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')
            yield item
        next_link = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        print(next_link)
        next_url = 'https://movie.douban.com/top250'+next_link
        print(next_url)
        yield scrapy.Request(next_url, callback=self.parse)
