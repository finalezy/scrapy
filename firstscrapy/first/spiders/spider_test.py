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
            item['score_num'] = str(movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')).replace('[','').replace(']','').replace('\'','')
            item['movie_direct'] =str(movie.xpath('.//div[@class="bd"]/p[1]/text()').re('(?<=导演\:).*(?=主演)')).replace(r'\xa0','').replace('[','').replace(']','').replace('\'','')
            item['movie_intro'] = movie.xpath('.//p[@class="quote"]/span/text()').extract_first()
            yield item
        next_link = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        if next_link:
            print(next_link)
            next_url = 'https://movie.douban.com/top250'+next_link
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
