from bs4 import BeautifulSoup
import urllib.request
import re


def scraper():
    r = urllib.request.urlopen("https://www.kitco.com/bitcoin-price-charts-usd/").read()
    import pdb
    pdb.set_trace()

    soup = BeautifulSoup(r, 'html.parser')

    btcPrice = soup.find('div', class_="tv-widget-watch-list__row js-quote-ticker tv-site-table__row tv-site-table__row--interactive tv-widget-watch-list__row--interactive tv-site-table__row--highlighted tv-widget-watch-list__row--highlighted symbol-active-color--hzu4 quote-ticker-inited")

    return btcPrice


def main():
    print(f"{scraper()}")


main()
