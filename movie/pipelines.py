# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno
from twisted.enterprise import adbapi
from scrapy import log
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline

class MoviePipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='moviespider',
                                            user='Arbrash', passwd='laozi1026',
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8', use_unicode=True)
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        #query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        if item.get('movie_name'):
             for i in range(len(item['movie_name'])):
                  tx.execute('insert into info values (%s, %s, %s, %s, %s, %s, %s, %s)',
                            (item['movie_name'], item['movie_rating'], item['movie_long'], item['movie_classify'],
                            item['movie_userrating'], item['movie_description'], item['movie_director'], item['movie_actor']))


