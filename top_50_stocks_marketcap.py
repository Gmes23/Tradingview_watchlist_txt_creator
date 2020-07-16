from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

r = requests.get('http://www.iweblists.com/us/commerce/MarketCapitalization.html', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

stock_tickers = soup.find_all('td', class_="body")

li = []

for stock_ticker in stock_tickers:
    li.append(stock_ticker.text)
    # print(stock_ticker.text, end='\n'*2)

li2 = li[::3]
print(li2)