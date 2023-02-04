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
        return f"Item('{self.name}',{self.price},{self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes /methods
        super().__init__(
            name,price,quantity
        )
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero"

        self.broken_phones = broken_phones
        Phone.all.append(self)


phone1 = Phone("jscPhoneva10", 500, 5, 1)
print(Item.all)
print(Phone.all)

