# Tradingview Watchlist Import TXT Files Creator from Exchanges

> Below you'll find Tradingview txt import files for Coinbase with USD pairings, Top 50 stock tickers by marketcap ( USA )

## Usage

This script creates a txt file of all the Coinbase coins with USD pairings, for easy import to Trading view watchlist.

## Getting Started
I used [Coinbase Pro API](https://github.com/danpaquin/coinbasepro-python/blob/master/README.md) library by Daniel Paquin for the data , 

- You may manually install the project or use ```pip```:
```python
pip install cbpro
#or
pip install git+git://github.com/danpaquin/coinbasepro-python.git
```

-then run the ```coinbase_request.py``` file

**The txt files can be imported into a Tradingview watchlist if you dont want to do it manually.**

<p align="center">
  <img src="https://i.imgur.com/jeZpljC.png" alt="Tradingview Watchlists" />
</p>

**Usage**:

* Click "View raw" on the list you want to import below and save the file
* In Tradingview, choose "Import watchlist" and pick the file you want to import