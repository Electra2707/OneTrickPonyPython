class Item:
    def __init__(self, name, price, quantity, numpad: bool):
        print(f"I AM CREATED!")
        self.name = name
        self.price = price
        self.quantity = 1
        if not quantity == 1:
            self.quantity = quantity
        self.numpad = numpad
        if not isinstance(numpad, bool):
            raise ValueError(
                f"the 4th argument in the {self} should be a boolean value")

    def calculate_total_price(self):
        return self.price * self.quantity
    # def calculate_total_price(self, x, y): bad
    #     return x * y bad

    def has_numpad(self):
        if self.numpad is True:
            print(f"The {self.name} has a numpad")
        else:
            print(f"The {self.name} dosen't has a numpad")


item1 = Item("Phone", 100, 5, False)
item2 = Item("Laptop", 1000, 3, True)

print(item1.name, item1.price, item1.quantity)
print(item2.name, item2.price, item2.quantity)

print(item1.calculate_total_price())
item1.has_numpad()
print(item2.calculate_total_price())
item2.has_numpad()
"""The time complexity of the code you provided is O(1), 
or constant time. This is because the operations being
performed in the __init__ method and calculate_total_price
method are simple assignments and arithmetic operations,
which take a constant amount of time regardless of the size of the inputs.
"""
