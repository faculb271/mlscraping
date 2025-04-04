# Web Scraping utilizando Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![lxml](https://img.shields.io/badge/lxml-4.6%2B-green)

## Actualizacion
La diferencia de este, con la version 1 de este Crawler es que, se agrego:
1. Uso de la POO
2. Creacion de Requirements.txt
3. Uso de try y except
4. Se agrego el `.xlsx`
5. Se agregaron dos campos que incluye la URL de la imagen y la URL del producto. Tambien se cambio seller.

---

Este proyecto extrae productos y guarda los datos en un archivo `.csv` y `.xlsx`

Incluye los siguientes campos:

- Nombre del producto
- Precio actual
- Precio anterior
- Descuento aplicado
- Marca / Vendedor
- URL de la imagen
- URL del producto

## Objetivo

Este proyecto fue creado **con fines de prácticar web scraping** utilizando Python. Su propósito es aprender a:

- Extraer datos estructurados desde HTML
- Utilizar XPath con `lxml`
- Automatizar navegación paginada
- Exportar resultados a CSV con `pandas`

### Librerías necesarias

Instalá las dependencias necesarias con:

```PowerShell
pip install pandas lxml curl_cffi
```
Nota: curl_cffi permite simular un navegador como Chrome (evita bloqueos por scraping básico).

## ¿Cómo usarlo?

1. Cloná este proyecto o copiá los archivos a tu máquina:
```PowerShell
git clone https://github.com/faculb271/mlscraping.git
```
2. Ejecutá el archivo crawler.py:
```PowerShell
python main.py
```
Al finalizar, vas a obtener dos archivos en diferentes datos con todos los datos scrapeados.

## ¿Qué hace el crawler?

Recorre automáticamente las páginas ?page=1 hasta ?page=10.

Obtiene el árbol HTML con lxml y simula un navegador con curl_cffi.

Extrae con XPath los siguientes campos por producto:

- Nombre del producto
- Precio actual
- Precio anterior
- Descuento aplicado
- Marca / Vendedor
- URL de la imagen
- URL del producto

Guarda todos los resultados en un archivo CSV y Excel.
