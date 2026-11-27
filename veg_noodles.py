from noodles import Noodles


class VegNoodles(Noodles):
    def __init__(self, price, cals, descr):
        super().__init__(price, cals, descr)
