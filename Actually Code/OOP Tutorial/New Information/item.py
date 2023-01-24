import csv


class Item:
    all = []

    def __init__(self, name: str, price: float = 0, quantity: int = 0):
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=item.get("price"),
                quantity=item.get("quantity"),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity
