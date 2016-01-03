# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class MovieItem(Item):
    movie_name = Field()
    movie_director = Field()
    movie_long = Field()
    movie_description = Field()
    movie_rating = Field()
    movie_classify = Field()
    movie_actor = Field()
    movie_userrating = Field()
    pass

