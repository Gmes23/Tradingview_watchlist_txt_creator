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

li2 = []
for i in range(2, len(li), 4):
    li2.append(li[i])

f = open("top_50_stocks_marketcap.txt", "a")
for ticker in li2:
    f.write(ticker)
    f.write('\n')
f.close()

print(li2)