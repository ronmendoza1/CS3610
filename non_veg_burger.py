from burger import Burger


class NonVegBurger(Burger):
    def __init__(self, price, cals, descr):
        super().__init__(price, cals, descr)
