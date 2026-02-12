# ARES-X File 16: Recursive Site Mapper
import requests
from bs4 import BeautifulSoup

def crawl_target(url):
    """Maps the directory structure of a web target."""
    print(f"[*] ARES-X: Crawling {url} for hidden directories...")
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return list(set(links)) # Returns unique paths found
    except Exception as e:
        return [f"Error: {str(e)}"]
