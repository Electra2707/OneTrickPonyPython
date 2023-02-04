from item import Item

class Keyboard(Item):
    PAY_RATE = 0.7
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )