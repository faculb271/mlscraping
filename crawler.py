from curl_cffi import requests
from lxml import html
import pandas as pd

class Crawler:
    def __init__(self,url):
        self.url = self.URL
        self.data = []

    def scraper(self, url):
        try:
            response = requests.get(url)
            tree = html.fromstring(response.text)
            products = tree.xpath('//div[contains(@class, "andes-card") and contains(@class, "poly-card")]')
            for product in products:
                self.extraer_datos(producto)
        except Exception as e:
            print(f"hubo un error con {e}")

    def _extraer_datos(self, product):
        name = product.xpath('.//a[@class="poly-component__title"]/text()')
        current_price = product.xpath('.//div[@class="poly-price__current"]//span[@class="andes-money-amount__fraction"]/text()')
        old_price = product.xpath('.//span[@class="andes-money-amount__fraction"]/text()')
        seller = product.xpath('.//span[@class="poly-component__seller"]/text()')
        discount = product.xpath('.//span[contains(@class, "andes-money-amount__discount")]/text()')


scraper = Crawler 
scraper.scraper()
