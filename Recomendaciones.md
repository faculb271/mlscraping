# Recomendaciones para mejorar el programa

```python
if __name__ == "__main__":
    #Esto puede ser una variable constante en el archivo Config.py (ir al titulo Config)
    base_url = "https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1"
    #No debes de pasar de esta manera el parametro de pages, modificar como se corrigio
    crawler = Crawler(base_url, pages=10)
    crawler.run() 
```

## Agregar `openpyxl` en el archivo requirements

```python

    def save_data(self, filename='productos.csv'):
        df = self._clean_data()
        df.to_csv(filename, index=False)
        excel_filename = filename.replace('.csv', '.xlsx')
        df.to_excel(excel_filename, index=False)
        #Agregar un log que indique que se ha guardado los archivos (Mirar el titulo Log)
```

# Limpieza de datos
Tienes que limpiar el campo `photo` ya que lo guarda en forma de lista, por ejemplo: `['https://http2.mlstatic.com/D_Q_NP_2X_645011-MLA81313612233_122024-AB.webp']`


--- 

# Config

Puedes crear un archivo llamado `Config.py` para almacenar variables constantes,
los cuales no van a cambiar su valor durante la ejecucion del programa.
Variables que puedes almacenar en `Config.py`:

BASE_URL="https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1"

HEADERS={
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

Un timeout de 120 es bastante aceptable
TIMEOUT = 120 

LOG_FILE = 'ejemplo.log'


## Como lo uso?

Una vez creado el archivo `Config.py` y agregado las variables, solo debes de importarlo en el archivo `Crawler.py`

```python
import config
```
Y luego lo usas de esta manera:

```python
response=requests.get(url=config.BASE_URL)
```

---


# Log
Tambien se comenzara a hacer uso de logs para ello debera de mirar el archivo log.py y ejemplo.py, no debes de modificar nada, solo mirar de que se trata el log y como se usa en ejemplo.


---


# EXITOS!!! 







