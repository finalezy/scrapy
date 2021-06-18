# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class Doubanpipeline(object):
    def __init__(self):
        self.f = open("movie_top250.csv","a",newline='',encoding='utf-8')
        self.fieldnames =['ranking','movie_name','score','score_num','movie_intro','movie_direct']
        self.writer = csv.DictWriter(self.f,fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self,item,spider):
        self.writer.writerow(item)
        return item

    def close_spider(self,spider):
        self.f.close()