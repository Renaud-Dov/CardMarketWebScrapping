from enum import Enum

import random


class Condition(Enum):
    MINT = 0
    NEAR_MINT = 1
    EXCELLENT = 2
    GOOD = 3
    LIGHT_PLAYED = 4
    PLAYED = 5
    POOR = 6
    MORE_INFOS = 7


def GetConditionFromString(condition):
    if condition == "Mint":
        return Condition.MINT
    elif condition == "Near Mint":
        return Condition.NEAR_MINT
    elif condition == "Excellent":
        return Condition.EXCELLENT
    elif condition == "Good":
        return Condition.GOOD
    elif condition == "Light Played":
        return Condition.LIGHT_PLAYED
    elif condition == "Played":
        return Condition.PLAYED
    elif condition == "Poor":
        return Condition.POOR
    else:
        return Condition.MORE_INFOS


class Offer:
    def __init__(self, seller: str, offer_link: str, price: float, lang: str, first_edition: bool, condition: Condition):
        super().__init__()
        self.seller = seller
        self.offer_link = offer_link
        self.price = price
        self.language = lang
        self.first_edition = first_edition
        self.condition = GetConditionFromString(condition)

    def Export(self):
        return {
            "seller": self.seller,
            "link": self.offer_link,
            "price": self.price,
            "language": self.language,
            "first_edition": self.first_edition,
            "condition": self.condition.value
        }

    def __str__(self):
        return f"{self.seller} {self.price} €"

    def __eq__(self, other):
        return self.language == other.language and self.first_edition == other.first_edition \
               and abs(self.condition.value - other.condition.value) <= 1
