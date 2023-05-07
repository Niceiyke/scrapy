# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class JumiaPipeline:
    def process_item(self, item, spider):
        print('pipeline' +item['name'])
        return item
    
class Remove_Items_NotinStock_Pipeline:

    def process_item(self,item,spider):
        adapter =ItemAdapter(item)

        print('wow',adapter['stock'])

        if adapter['stock']== "Add To Cart":
            return item
            
        else:
            raise DropItem(' {item} sold out')
            
class Remove_Items_withNoDiscount_Pipeline:

    def process_item(self,item,spider):
        adapter =ItemAdapter(item)

        if adapter['original_price'] is not None:
            return item
            
        else:
            raise DropItem('No Discount found for {item}')