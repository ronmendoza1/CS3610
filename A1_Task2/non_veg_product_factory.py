from product_factory import ProductFactory
from non_veg_burger import NonVegBurger
from non_veg_pizza import NonVegPizza
from non_veg_noodles import NonVegNoodles
from non_veg_cutlet import NonVegCutlet


class NonVegProductFactory(ProductFactory):
    def createBurger(self, p, c, d) -> NonVegBurger:
        return NonVegBurger(p, c, d)

    def createPizza(self, p, c, s, d) -> NonVegPizza:
        return NonVegPizza(p, c, s, d)

    def createNoodles(self, p, c, d) -> NonVegNoodles:
        return NonVegNoodles(p, c, d)

    def createCutlet(self, p, c, d) -> NonVegCutlet:  # Non-Veg only
        return NonVegCutlet(p, c, d)
