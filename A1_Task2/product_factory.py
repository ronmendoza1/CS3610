from abc import ABC, abstractmethod


class ProductFactory(ABC):

    @abstractmethod
    def create_burger(self, p, c, d):
        pass

    @abstractmethod
    def create_pizza(self, p, c, s, d):
        pass

    @abstractmethod
    def create_noodles(self, p, c, d):
        pass

    @abstractmethod
    def create_cutlet(self, p, c, d):
        pass
