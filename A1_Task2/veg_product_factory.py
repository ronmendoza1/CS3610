from product_factory import ProductFactory
from products import VegBurger, VegPizza, VegNoodles


class VegProductFactory(ProductFactory):

    def create_burger(self, p, c, d):
        return VegBurger(p, c, d)

    def create_pizza(self, p, c, s, d):
        return VegPizza(p, c, s, d)

    def create_noodles(self, p, c, d):
        return VegNoodles(p, c, d)

    def create_cutlet(self, p, c, d):
        raise ValueError("Vegetarian cutlet is unavailable.")
