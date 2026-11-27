from iproduct import IProduct


# Abstract Burger
class Burger(IProduct):

    def __init__(self, price, calories, descr):
        self.price = price
        self.calories = calories
        self.descr = descr

    def get_price(self):
        return self.price

    def get_description(self):
        return self.descr


# Abstract Pizza
class Pizza(IProduct):

    def __init__(self, price, calories, size, descr):
        self.price = price
        self.calories = calories
        self.size = size
        self.descr = descr

    def get_price(self):
        return self.price

    def get_description(self):
        return self.descr


# Vegetarian Products
class VegBurger(Burger):
    pass


class VegPizza(Pizza):
    pass


class VegNoodles(IProduct):

    def __init__(self, price, calories, descr):
        self.price = price
        self.calories = calories
        self.descr = descr

    def get_price(self):
        return self.price

    def get_description(self):
        return self.descr


# Non-Vegetarian Products
class NonVegBurger(Burger):
    pass


class NonVegPizza(Pizza):
    pass


class NonVegNoodles(IProduct):

    def __init__(self, price, calories, descr):
        self.price = price
        self.calories = calories
        self.descr = descr

    def get_price(self):
        return self.price

    def get_description(self):
        return self.descr


class NonVegCutlet(IProduct):

    def __init__(self, price, calories, descr):
        self.price = price
        self.calories = calories
        self.descr = descr

    def get_price(self):
        return self.price

    def get_description(self):
        return self.descr
