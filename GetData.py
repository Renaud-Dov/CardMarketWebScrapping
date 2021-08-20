from bs4 import BeautifulSoup
import urllib.request

import Card
import json
import time


class Data:

    def __init__(self, user: str, collection: str):
        self.user = user
        self.website = f"https://www.cardmarket.com/fr/{collection}/Users/{user}/Offers/Singles"
        self.cards = list()

    def Fetch(self):
        self.cards = list()
        self.__ParseWebPage()

    def __ParseWebPage(self, i: int = 1):
        print("Parsing page", i)
        page = urllib.request.urlopen(self.website + f"?site={i}")

        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find('div', attrs={'class': 'table-body'})
        results = table.find_all('div', {"class": "row no-gutters article-row"})
        for result in results:
            try:
                card = Card.Card(result, self.user)
                self.cards.append(card)
                print(card)
            except Exception as e:
                print(f"error : {e}")

        if len(results) != 0:
            self.__ParseWebPage(i + 1)

    def Export(self):
        export = list()
        for card in self.cards:
            a = card.Export()
            if len(a[2]) > 0:
                export.append({"name": a[0], "link": a[3], "MyCard": a[1], "offers": a[2]})

        with open("output.json", 'w') as outfile:
            json.dump({"timestamp": time.time(), "cards": export}, outfile)
