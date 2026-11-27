from abc import ABC, abstractmethod
from burger import Burger
from pizza import Pizza
from noodles import Noodles


class ProductFactory(ABC):
    @abstractmethod
    def createBurger(self, p, c, d) -> Burger: ...

    @abstractmethod
    def createPizza(self, p, c, s, d) -> Pizza: ...

    @abstractmethod
    def createNoodles(self, p, c, d) -> Noodles: ...
