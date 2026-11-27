from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def get_Price(self) -> int: ...

    @abstractmethod
    def get_Description(self) -> str: ...
