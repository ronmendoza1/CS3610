from typing import Dict, List
from i_product import IProduct
from product_factory import ProductFactory
from veg_product_factory import VegProductFactory
from non_veg_product_factory import NonVegProductFactory


class FoodApp:
    def __init__(self):
        veg, nonveg = VegProductFactory(), NonVegProductFactory()
        # {prodName: ProductFactory}
        self.AvailableFood: Dict[str, ProductFactory] = {
            "Veg Burger": veg,
            "Veg Pizza": veg,
            "Veg Noodles": veg,
            "Non-Veg Burger": nonveg,
            "Non-Veg Pizza": nonveg,
            "Non-Veg Noodles": nonveg,
            "Non-Veg Cutlet": nonveg,
        }

    def _create(self, name: str) -> IProduct:
        factory = self.AvailableFood[name]
        non_veg = name.startswith("Non")
        if name.endswith("Burger"):
            return factory.createBurger(180 if non_veg else 120, 350, name)
        if name.endswith("Pizza"):
            return factory.createPizza(350 if non_veg else 250, 700, "Medium", name)
        if name.endswith("Noodles"):
            return factory.createNoodles(200 if non_veg else 150, 450, name)
        if name.endswith("Cutlet"):
            return factory.createCutlet(160, 400, name)
        raise ValueError(f"Unknown product type: {name}")

    def makeOrder(self, prodNames: List[str]) -> List[IProduct]:
        order = []
        for name in prodNames:
            if name not in self.AvailableFood:
                raise ValueError(f"'{name}' is not available.")
            order.append(self._create(name))
        return order

    def getOrderDescription(self, order: List[IProduct]) -> str:
        lines = [f"{p.get_Description()} - {p.get_Price()}" for p in order]
        lines.append(f"Total: {sum(p.get_Price() for p in order)}")
        return "\n".join(lines)
