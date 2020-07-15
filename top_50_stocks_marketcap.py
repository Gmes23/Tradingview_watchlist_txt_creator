from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get('http://www.iweblists.com/us/commerce/MarketCapitalization.html', headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())