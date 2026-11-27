from burger import Burger


class VegBurger(Burger):
    def __init__(self, price, cals, descr):
        super().__init__(price, cals, descr)

    def showVegBurgerAdver(self) -> str:
        return "Veg Burger: fresh, tasty and 100% vegetarian!"
