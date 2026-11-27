from food_app import FoodApp
from veg_product_factory import VegProductFactory
from nonveg_product_factory import NonVegProductFactory


def main():

    print("========== FOOD APP ==========")

    print("\nSelect Food Category:")
    print("1. Vegetarian")
    print("2. Non-Vegetarian")

    choice = input("\nEnter choice: ")

    if choice == "1":

        factory = VegProductFactory()

        print("\n========== VEGETARIAN MENU ==========")
        print("Veg Burger")
        print("Veg Pizza")
        print("Veg Noodles")

    elif choice == "2":

        factory = NonVegProductFactory()

        print("\n========== NON-VEGETARIAN MENU ==========")
        print("Non-Veg Burger")
        print("Non-Veg Pizza")
        print("Non-Veg Noodles")
        print("Non-Veg Cutlet")

    else:
        print("Invalid selection.")
        return

    app = FoodApp(factory)

    print("\nEnter products separated by commas.")
    user_input = input("Your order: ")

    product_names = user_input.split(",")

    order = app.make_order(product_names)

    if order:
        app.get_order_description(order)
    else:
        print("No valid products ordered.")

    print("\nThank you for ordering!")


if __name__ == "__main__":
    main()
