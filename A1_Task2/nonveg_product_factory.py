from product_factory import ProductFactory
from products import (
    NonVegBurger,
    NonVegPizza,
    NonVegNoodles,
    NonVegCutlet
)


class NonVegProductFactory(ProductFactory):

    def create_burger(self, p, c, d):
        return NonVegBurger(p, c, d)

    def create_pizza(self, p, c, s, d):
        return NonVegPizza(p, c, s, d)

    def create_noodles(self, p, c, d):
        return NonVegNoodles(p, c, d)

    def create_cutlet(self, p, c, d):
        return NonVegCutlet(p, c, d)
