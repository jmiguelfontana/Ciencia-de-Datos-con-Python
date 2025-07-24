import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys 

url = 'https://books.toscrape.com'

headers = {
    'User-Agent': 'Mozilla/100.0 Chrome/120.0.0 Safari/537.36'
}

def fetch_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting all article titles from elperiodico.com
        libros = soup.find_all('article', class_='product_pod')
        #print("Titles from elperiodico.com:")
        #print(titles)

        for libro in libros:
            print(libro.h3.a['title']+"  "+libro.find('p', class_='price_color').get_text(strip=True))
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)

fetch_data(url)
