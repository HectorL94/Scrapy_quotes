import scrapy
# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()
class QuotesSpyder(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self,response):
        print("\n\n")
        print("*"*10)
        
        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')
        print("\n\n")
        print("*"*10)

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas:')
        for quote in quotes:
            print(f'- {quote}')
        print("\n\n")
        print("*"*10)

        top_ten_tags = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
        for tag in top_ten_tags:
            print(f'- {tag}')
        #print(response.status, response.headers)
        print("*"*10)
        print("\n\n")