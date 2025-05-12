from curl_cffi import requests
from lxml import html
import pandas as pd
import config
import log

class Crawler:
    def __init__(self):
        self.base_url = config.BASE_URL
        self.pages = config.PAGES
        self.data = []
        self.__log = log.Log().get_logger(config.LOG_FILE)

    def get_products(self, page):
        """Obtiene el HTML de una pagina"""
        try:
            url = f"{self.base_url}&page={page}"
            response = requests.get(url,impersonate="chrome110")
            tree = html.fromstring(response.text)
            products = tree.xpath('//div[contains(@class, "andes-card") and contains(@class, "poly-card")]')
            self.__log.info(f"pagina {page} obtenida exisotasamente")
            return products
        except Exception as e:
            self.__log.error(f"Esta fallando algo con la pagina {page}")

    def extract_data(self, products):
        """Extrae los productos de dicha pagina"""
        for product in products:
            try:
                name = product.xpath('.//a[@class="poly-component__title"]/text()')
                current_price = product.xpath('.//div[@class="poly-price__current"]//span[@class="andes-money-amount__fraction"]/text()')
                old_price = product.xpath('.//span[@class="andes-money-amount__fraction"]/text()')
                seller = product.xpath('.//span[@class="poly-component__brand"]/text()')
                discount = product.xpath('.//span[contains(@class, "andes-money-amount__discount")]/text()')
                photo = product.xpath('.//img[contains(@class, "poly-component__picture")]/@data-src')
                url = product.xpath('.//a[contains(@class, "poly-component__title")]/@href')

                self.data.append({
                    'product': name[0] if name else None,
                    'seller': seller[0] if seller else None,
                    'price': current_price[0] if current_price else None,
                    'old_price': old_price[0] if old_price else None,
                    'discount (%)': discount[0] if discount else None,
                    'photo': photo[0] if photo else None,
                    'url': url[0] if url else None
                })

                self.__log.info(f"Extraccion exitosa")
            except Exception as e:
                self.__log.error(F"Hay un posible problema con los xpath o con {e}")

    def _clean_data(self):
        """Limpieza los datos del DataFrame"""
        df = pd.DataFrame(self.data)
        df['price'] = df['price'].replace({',': '', '€': '', '$': ''}, regex=True).astype(float, errors='ignore')
        df['old_price'] = df['old_price'].replace({',': '', '€': '', '$': ''}, regex=True).astype(float, errors='ignore')
        df['discount (%)'] = df['discount (%)'].str.replace('% OFF','',regex=False).astype(int,errors='ignore')
        
        return df

    def save_data(self, filename='productos.csv'):
        df = self._clean_data()
        df.to_csv(filename, index=False)
        excel_filename = filename.replace('.csv', '.xlsx')
        df.to_excel(excel_filename, index=False)

    def run(self):
        """Método principal que ejecuta y guarda los datos"""
        for page in range(1, self.pages + 1):
            products = self.get_products(page)
            self.extract_data(products)
        self.save_data()
        self.__log.info(f"Crawler ejecutado")
        
if __name__ == "__main__":
    crawler = Crawler() 
    crawler.run()
