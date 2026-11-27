from pizza import Pizza


class VegPizza(Pizza):
    def __init__(self, price, cals, size, descr):
        super().__init__(price, cals, size, descr)

    def showVegPizzaAdver(self) -> str:
        return "Veg Pizza: loaded with garden-fresh toppings!"
