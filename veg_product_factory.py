from product_factory import ProductFactory
from veg_burger import VegBurger
from veg_pizza import VegPizza
from veg_noodles import VegNoodles


class VegProductFactory(ProductFactory):
    def createBurger(self, p, c, d) -> VegBurger:
        return VegBurger(p, c, d)

    def createPizza(self, p, c, s, d) -> VegPizza:
        return VegPizza(p, c, s, d)

    def createNoodles(self, p, c, d) -> VegNoodles:
        return VegNoodles(p, c, d)
