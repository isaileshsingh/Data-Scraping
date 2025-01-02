import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_quotes(url):
    r = requests.get(url, proxies=None)
    soup = BeautifulSoup(r.text, features="html.parser")
    quotes_container = soup.find("div", _class="quotes")
    quotes = quotes_container.find("div", _class="quote")

    results = []
    for quote in quotes:

        quote_text = quote.find("div", _class= "quoteText").text
        details = {}
        details["quote"] = quote_text.split("-")[0].strip()
        details["author"] = quote_text.split("-")[1].strip()

        # tags = quote.find_all("div", _class="smallText")
        tags = quote.find("div", _class="smallText")
        try:
            details["tags"] = tags.text.replace("tags:","")
        except Exception as e:
            # print(e)
            pass


        results.append(details)

    return results

if __name__ == "__main__":
    result = scrape_quotes("https://www.goodreads.com/quotes")
    quote = result[10]
    tags = quote["tags"]
    print(result)
