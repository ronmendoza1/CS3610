from food_app import FoodApp


def main():
    app = FoodApp()

    order = app.makeOrder(["Veg Burger", "Veg Pizza", "Non-Veg Noodles", "Non-Veg Cutlet"])
    print("Your order:")
    print(app.getOrderDescription(order))

    print()
    print(order[0].showVegBurgerAdver())
    print(order[1].showVegPizzaAdver())

    try:
        app.makeOrder(["Veg Cutlet"])
    except ValueError as e:
        print("\nError:", e)


if __name__ == "__main__":
    main()
