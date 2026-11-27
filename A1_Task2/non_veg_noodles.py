from noodles import Noodles


class NonVegNoodles(Noodles):
    def __init__(self, price, cals, descr):
        super().__init__(price, cals, descr)
