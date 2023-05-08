# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3


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
        

class SavingToDb:

    def __init__(self):
        self.con =sqlite3.connect('scrapy.db')

        self.cur =self.con.cursor()
        self.create_table()

    def create_table(self):

        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
        name TEXT PRIMARY KEY,stock text,category text,store text,image text,url text,discount REAL,original_price REAL,discount_price REAL)""")

    def process_item(self,item,spider):
        self.cur.execute(""" INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?)""",
                         (item['name'],item['stock'],item['category'],item['store'],item['image'],item['url'],item['discount_percent'],item['original_price'],item['discount_price'],))
        
        self.con.commit()

        return item