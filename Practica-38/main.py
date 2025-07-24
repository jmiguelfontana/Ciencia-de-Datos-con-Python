import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys 

url = 'https://elpais.es/'

headers = {
    'User-Agent': 'Mozilla/100.0 Chrome/120.0.0 Safari/537.36'
}

def fetch_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        titles = [title.get_text(strip=True) for title in soup.find_all('h2')]
        
        articles = [{'Index': i, 'Titulo': t} for i, t in enumerate(titles)]
        df = pd.DataFrame(articles, columns=['Titulo'])
            
        return df
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)

articulos = fetch_data(url)
print(articulos.head(10))  # Display the first 10 articles