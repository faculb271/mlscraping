from curl_cffi import requests
from lxml import html
from lxml import etree
import pandas as pd

URL = "https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1&page=1"


response = requests.get(URL,impersonate="chrome110")
tree = html.fromstring(response.text) #Ultra importante para usar Xpath
products = tree.xpath('//*[@id="root-app"]/div/section/div[2]/div/div')

data = []
for product in products:
    current_price = product.xpath('//*[@id=":Ra1j7:"]/div[2]/div[2]/div/span[1]')
    old_price = product.xpath('//*[@id=":Ra1j7:"]/div[2]/div[2]/s/span[2]')
    seller = product.xpath('//*[@id=":Ra1j7:"]/div[2]/span[1]')
    name = product.xpath('//*[@id=":Ra1j7:"]/div[2]/a/text()')

    data.append({'product':name,
                 'seller':seller,
                 'price':current_price,
                 'old_price':old_price})

print(data)
pass