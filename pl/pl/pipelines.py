# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PlPipeline(object):
    def process_item(self, item, spider):
        print("Pipeline"+ item['macht_20'][0])
        return item
