from cutlet import Cutlet


class NonVegCutlet(Cutlet):
    def __init__(self, price, cals, descr):
        super().__init__(price, cals, descr)
