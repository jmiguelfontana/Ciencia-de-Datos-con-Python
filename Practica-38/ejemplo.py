import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys 

url = 'https://elperiodico.com/es/'
url2 = 'https://lavanguardia.com/'
url3 = 'https://infojobs.net/'
url4 = 'https://www.carrefour.es/'

headers = {
    'User-Agent': 'Mozilla/100.0 Chrome/120.0.0 Safari/537.36'
}

def fetch_data(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting all article titles from elperiodico.com
        titles = [title.get_text(strip=True) for title in soup.find_all('h2')]
        #print("Titles from elperiodico.com:")
        #print(titles)

        for title in titles:
            print(">"+title)
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)

fetch_data(url4)




