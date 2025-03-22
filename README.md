# Web Scraper de Mercado Libre con Python

Este proyecto extrae productos y guarda los datos en un archivo `.csv`.

Incluye los siguientes campos:

- Nombre del producto
- Precio actual
- Precio anterior
- Descuento aplicado
- Marca / Vendedor


## 🎯 Objetivo

Este proyecto fue creado **con fines de prácticar web scraping** utilizando Python. Su propósito es aprender a:

- Extraer datos estructurados desde HTML
- Utilizar XPath con `lxml`
- Automatizar navegación paginada
- Exportar resultados a CSV con `pandas`

### ✅ Librerías necesarias

Instalá las dependencias necesarias con:

```PowerShell
pip install pandas lxml curl_cffi
```
Nota: curl_cffi permite simular un navegador como Chrome (evita bloqueos por scraping básico).

## 🚀 ¿Cómo usarlo?

1. Cloná este proyecto o copiá los archivos a tu máquina:
```PowerShell
git clone https://github.com/faculb271/mlscraping.git
```
2. Ejecutá el archivo main.py:
```PowerShell
python main.py
```
Al finalizar, vas a obtener un archivo productos.csv con todos los datos scrapeados.

## ¿Qué hace el scraper?

Recorre automáticamente las páginas ?page=1 hasta ?page=10.

Obtiene el árbol HTML con lxml y simula un navegador con curl_cffi.

Extrae con XPath los siguientes campos por producto:

- Nombre del producto
- Precio actual
- Precio anterior
- Descuento aplicado
- Marca / Vendedor

Guarda todos los resultados en un archivo CSV.
