from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52'
req = Request(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})

response = urlopen(req, timeout=20).read()
response_close = urlopen(req, timeout=20).close()

page_soup = soup(response, "html.parser")
balance = page_soup.find()
print(page_soup)
