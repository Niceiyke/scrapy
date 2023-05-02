import scrapy
from ..items import JumiaItem
from scrapy.loader import ItemLoader


class jumiaSpyder(scrapy.Spider):
    name ='jumia'
    start_urls =['https://www.jumia.com.ng/mlp-stay-connected-deals/android-phones/?seller_score=4-5&rating=4-5#catalog-listing']


    def parse(self, response):
        
        products =response.css('article.c-prd')

        for product in products:
            product_url=product.css('a.core').attrib['href']
            yield response.follow(f'https://www.jumia.com.ng{product_url}',callback=self.product_detail)


        next_page= response.css('a.pg::attr(href)').getall()[-2]
        print(next_page)

        if next_page is not None:
                yield response.follow(f'https://www.jumia.com.ng{next_page}',callback=self.parse)


    def product_detail(self,response):
            
            l= ItemLoader(item=JumiaItem(),selector=response)            

            l.add_css('name','h1.-pbxs'),
            l.add_css('discount_price','span.-fs24'),
            l.add_css('original_price','span.-fs16'),
            l.add_css('stock','button.add ::text')
            #l.add_value (f"'store','{self.name}'")

            yield l.load_item()
            
        