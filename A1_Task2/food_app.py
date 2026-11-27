from nonveg_product_factory import NonVegProductFactory

class FoodApp:

    def __init__(self, factory):
        self.factory = factory

    def make_order(self, product_names):

        order = []

        for name in product_names:

            name = name.strip().lower()
            
            if "burger" in name:
                product = self.factory.create_burger(
                    10, 250, "Delicious Burger"
                )

            elif "pizza" in name:
                product = self.factory.create_pizza(
                    15, 300, "Medium", "Delicious Pizza"
                )

            elif "noodles" in name:
                product = self.factory.create_noodles(
                    12, 200, "Delicious Noodles"
                )

            elif "cutlet" in name:

                if isinstance(self.factory, NonVegProductFactory):
                    product = self.factory.create_cutlet(
                        8, 180, "Delicious Cutlet"
                    )
                else:
                    print("Cutlet is not available.")
                    continue

            else:
                print(name, "is not available.")
                continue

            order.append(product)

        return order

    def get_order_description(self, order):

        total = 0

        print("\n========== YOUR ORDER ==========")

        for product in order:

            print("\nProduct:", product.get_description())
            print("Price: $", product.get_price())

            total += product.get_price()

        print("\nTotal Items:", len(order))
        print("Total Price: $", total)
