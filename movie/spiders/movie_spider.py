# encoding=utf8

from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from movie.items import MovieItem
import re


class MovieSpider(BaseSpider):
    name = "movie"
    allowed_domains = ["imdb.com"]
    start_urls = [
        "http://www.imdb.com/movies-in-theaters/"
    ]

    def parse(self, response):
        hxs = Selector(response)
        movies = hxs.xpath('//td[@class="overview-top"]')
        items = []

        for movie in movies:
            item = MovieItem()
            item['movie_name'] = ''.join(movie.xpath('h4/a/text()').extract())
            item['movie_rating'] = ''.join(movie.xpath('p[@class="cert-runtime-genre"]/img/@title').extract())
            item['movie_long'] = ''.join(movie.xpath('p[@class="cert-runtime-genre"]/time/text()').extract())

            classifies = movie.xpath('p[@class="cert-runtime-genre"]')
            for classify in classifies:
                item['movie_classify'] = '|'.join(classify.xpath('span[@itemprop="genre"]/text()').extract())
            item['movie_userrating'] = ''.join(movie.xpath('div[@class="rating_txt"]/div[@class="rating rating-list"]/@title').extract())
            item['movie_description'] = ''.join(movie.xpath('div[@class="outline"]/text()').extract())
            item['movie_director'] = ''.join(movie.xpath('div[@class="txt-block"]/span[@itemprop="director"]/span/a/text()').extract())

            actors = movie.xpath('div[@class="txt-block"]/span[@itemprop="actors"]')
            item['movie_actor'] = '|'.join(actors.xpath('span/a/text()').extract())
            items.append(item)

        return items
