from curl_cffi import requests
from lxml import html
import pandas as pd

URL = "https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1&page=1"


response = requests.get(URL,impersonate="chrome110")
tree = html.fromstring(response.text) #Ultra importante para usar Xpath
products = tree.xpath('//div[contains(@class, "andes-card") and contains(@class, "poly-card")]')

data = []
for product in products:
    name = product.xpath('.//a[@class="poly-component__title"]/text()')
    current_price = product.xpath('.//span[@class="andes-money-amount__fraction"]/text()')
    old_price = product.xpath('.//s/span[2]/text()')
    seller = product.xpath('.//span[contains(@class, "poly-component__seller")]/text()')
    discount = product.xpath('.//span[contains(@class, "andes-money-amount__discount")]/text()')

    data.append({
        'product': name[0] if name else None,
        'seller': seller[0] if seller else None,
        'price': current_price[0] if current_price else None,
        'old_price': old_price[0] if old_price else None,
        'discount': discount[0] if discount else None
    })

print(data)