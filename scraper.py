import requests
from bs4 import BeautifulSoup
from utils import clean_url

def scrape_urls(start_url):
    urls = set() 
    try:
        response = requests.get(start_url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            url = link["href"]
            if "sesisp.org" in url:  
                urls.add(clean_url(url))  

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {start_url}: {e}")

    return urls
