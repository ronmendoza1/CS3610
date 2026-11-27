from pizza import Pizza


class NonVegPizza(Pizza):
    def __init__(self, price, cals, size, descr):
        super().__init__(price, cals, size, descr)
