from Offers import Offer
from bs4 import BeautifulSoup, Tag
import urllib.request
import threading

verrou = threading.Lock()


class Card:
    def __init__(self, tag: Tag, myName: str):
        a_class = tag.find("a")
        self.name = a_class.string
        self.link = "https://www.cardmarket.com" + a_class.attrs["href"]
        findTag = tag.find("div", {"class": "product-attributes col"})
        self.rarete = findTag.contents[1].attrs["data-original-title"]

        cardCondition = findTag.contents[2].next.attrs["data-original-title"]
        lang = findTag.contents[3].attrs["data-original-title"]
        first_edition = tag.find("span", {"class": "icon st_SpecialIcon mr-1"}) is not None

        price = float(
            tag.find("span", {"class": "font-weight-bold color-primary small text-right text-nowrap"}).next.rstrip(
                "€").replace('.', '').replace(',', '.'))

        self.my_offer: Offer = Offer(myName, self.link, price, lang, first_edition, cardCondition)
        self.offers = list()
        self.__GetOtherOffers()

    def GetBetterOffers(self):
        l = list()
        for offer in self.offers:
            if offer == self.my_offer and offer.seller != self.my_offer.seller:  # same card quality
                l.append(offer)
        l.sort(key=lambda e: e.price, reverse=True)
        return l

    def __GetOtherOffers(self):
        page = urllib.request.urlopen(self.link)

        soup = BeautifulSoup(page, 'html.parser')
        self.img = "https:" + soup.find('img').attrs["data-echo"]
        table = soup.find('div', attrs={'class': 'table-body'})
        results = table.find_all('div', {"class": "row no-gutters article-row"})
        for result in results:
            seller = result.find("span", {"class": "d-flex has-content-centered mr-1"}).text

            price = float(result.find("span", {
                "class": "font-weight-bold color-primary small text-right text-nowrap"}).text.rstrip("€").replace('.',
                                                                                                                  '').replace(
                ',', '.'))
            findTag = result.find("div", {"class": "product-attributes col"})
            condition = findTag.contents[0].next.attrs["data-original-title"]
            lang = findTag.contents[1].attrs["data-original-title"]
            first_edition = len(findTag) > 2
            self.offers.append(Offer(seller, self.link, price, lang, first_edition, condition))

    def __str__(self):
        return str(self.my_offer) + "|" + str(len(self.offers))

    def Export(self):
        obj = []
        for offer in self.GetBetterOffers():
            obj.append(offer.Export())
        return self.name, self.my_offer.Export(), obj, self.img
