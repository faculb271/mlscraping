# Correciones a realizar

## Nota
Para poder ver el contenido de manera correcta en VS Code, debes hacer click derecho y colocar *Open Preview*

Las correcciones se realizaran sobre el codigo, haciendo uso de comentarios

```py
from curl_cffi import requests
from lxml import html
import pandas as pd

data = []

for page in range(1,11):
    # Definiste dos veces, a la larga te dara error
    URL = URL = f"https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1&page={page}"
    response = requests.get(URL,impersonate="chrome110")
    tree = html.fromstring(response.text)
    products = tree.xpath('//div[contains(@class, "andes-card") and contains(@class, "poly-card")]')

    for product in products:

        name = product.xpath('.//a[@class="poly-component__title"]/text()')
        current_price = product.xpath('.//div[@class="poly-price__current"]//span[@class="andes-money-amount__fraction"]/text()')
        old_price = product.xpath('.//span [@class="andes-money-amount__fraction"]/text()')
        seller = product.xpath('.//span[@class="poly-component__seller"]/text()')
        discount = product.xpath('.//span[contains(@class, "andes-money-amount__discount")]/text()')
        # Esta parte esta bien, pero debes de formatear los datos, mira la seccion de ejemplos 
        data.append({
            'product': name[0] if name else None,
            'seller': seller[0] if seller else None ,
            'price': current_price[0] if current_price else None,
            'old_price': old_price[0] if old_price else None,
            'discount': discount[0] if discount else None,})

df = pd.DataFrame(data)
#Falto crear el archivo excel
df.to_csv('productos.csv',index=False)

```
# Requerimientos

Se requiere que se haga uso de el archivo `requirements.txt` donde se colocaran las librerias usadas en este proyecto.
Como por ejemplo `pandas`, `lxml`, etc.




# Recomendaciones

Hacer uso de la Programacion Orientada a Objeto (POO)

Para ello te puedes guiar del siguiente codigo:

```python

class Crawler:

  def __init__(self):
    self.data=[]


  def run(self):
    pass


```
 Como se puede observar, los dos metodos que se deben de colocar si o si, son __ **__init__** __ y **run**. Luego puedes agregar tantas funciones como quieras.
 
Luego para poder ejecutar el codigo, se recomienda hacer uso de la siguiente estructura:

```python
'''Es una estructura común en Python que se usa para ejecutar código solo
cuando el archivo es ejecutado directamente, y no cuando es importado como módulo en otro archivo.'''
if __name__ == '__main__':
    #Crear el objeto de la clase y ejecutar el metodo run
    pass
```

# Campos (Ejemplo)

Los campos se deben de formatear y no solo colocarlos como salen la pagina.
Dado el siguiente ejemplo de datos que se extrajo de la pagina:
`Cerveza Miller Genuine Draft Lata 473ml Pack X24,Por LA BARRA ,33.415,54.768,38% OFF`\

Este deberia de ser su formato:
```python
        product = {
            'name':'Cerveza Miller Genuine Draft Lata 473ml Pack X24' ,
            'seller': 'LA BARRA' ,
            'price': 33.415,
            'old_price': 54.768,
            'discount': 38
        }
```
Ademas se require estos dos campos: `url_image` `link_profile` ambos son links

Se recomienda para la extraccion de campos, hacer uso de **try except**, esto evitara que el codigo se rompa por completo.
Puedes guiarte de aqui:

```python
    try:
        pass
    except Exception as e:
        print(f'Esto es el error: {e}')
```


