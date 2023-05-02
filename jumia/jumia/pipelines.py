# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class JumiaPipeline:
    def process_item(self, item, spider):
        return item
    
class Remove_Items_without_Discount_Pipeline:

    def process_item(self,item,spider):
        adapter =ItemAdapter(item)

        if adapter.get('stock'):

            adapter['stock']=="Add to cart"
            return item
            
        else:
            raise DropItem(' {item} sold out')
            
