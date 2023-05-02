# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst,MapCompose
from w3lib.html import remove_tags



def process_price(value):
    valu=value.split('₦')[-1].strip().replace(",",'')
    valu =float(valu)
    return valu
def remove_new_line(value):
    return value.replace('\"','')

class JumiaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags,remove_new_line), output_processor=(TakeFirst()))
    original_price =scrapy.Field(input_processor=MapCompose(remove_tags, process_price),output_processor=(TakeFirst()))
    discount_price =scrapy.Field(input_processor=MapCompose(remove_tags, process_price),output_processor=(TakeFirst()))
    stock = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=(TakeFirst()))
    #store=scrapy.Field()

   
