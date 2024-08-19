# import os
# from dotenv import load_dotenv
# load_dotenv()
# PROXY = os.getenv('PROXY')
# proxies = {
#     "http" : PROXY,
#     "https" : PROXY
# }

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    r = requests.get(url, proxies=None)
    print(r.status_code)

if __name__ == "__main__":
    scrape_quotes("https://www.goodreads.com/quotes")