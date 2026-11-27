from abc import ABC
from i_product import IProduct


class Pizza(IProduct, ABC):
    def __init__(self, price=0, calories=0, size="Small", descr=""):
        self._price = price
        self._calories = calories
        self._size = size
        self._descr = descr

    def get_Price(self) -> int:
        return self._price

    def get_Description(self) -> str:
        return f"{self._descr} ({self._size})"
