import csv


class Item:
    all = []

    def __init__(self, name: str, price, quantity):
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

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


Item.instantiate_from_csv()
print(Item.all)
