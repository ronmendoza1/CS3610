from abc import ABC
from i_product import IProduct


class Noodles(IProduct, ABC):
    def __init__(self, price=0, calories=0, descr=""):
        self._price = price
        self._calories = calories
        self._descr = descr

    def get_Price(self) -> int:
        return self._price

    def get_Description(self) -> str:
        return self._descr
