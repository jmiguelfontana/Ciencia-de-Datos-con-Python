import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys 

url_fiction = 'https://books.toscrape.com/catalogue/category/books/fiction_10/'
url_travel = 'https://books.toscrape.com/catalogue/category/books/travel_2/'

headers = {
    'User-Agent': 'Mozilla/100.0 Chrome/120.0.0 Safari/537.36'
}

def fetch_data(url, pagina = 1):
    try:
        response = requests.get(url+'page-'+str(pagina)+'.html', headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting all article titles from elperiodico.com
        libros = soup.find_all('article', class_='product_pod')

        resumen = [{'Index': i, 'Titulo': t.h3.a['title']} for i, t in enumerate(libros)]
        df = pd.DataFrame(resumen, columns=['Titulo'])

        return df
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

libros = pd.DataFrame()

intPagina = 1
for intPagina in range(1, 10):
    librosPagina = fetch_data(url_fiction, intPagina)
    libros = pd.concat([libros, librosPagina], ignore_index=True)

intPagina = 1
for intPagina in range(1, 10):
    librosPagina = fetch_data(url_travel, intPagina)
    libros = pd.concat([libros, librosPagina], ignore_index=True)

libros.to_excel('practica-39.xlsx', index=False)

#fetch_data(url_travel, 1)