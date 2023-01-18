class Item:
    def __init__(self, name: str, price: float or int, quantity: int, numpad: bool):

        # Run validations to the recived arguments
        assert type(name) is str, f"name should be a string, got {type(name)}"
        assert price >= 0 and (type(price) is float or type(
            price) is int), f"price should be a float/int greater or equal than 0, got {price} ({type(price)})"
        assert quantity >= 0 and type(
            quantity) is int, f"quantity should be an integer greater or equal than 0, got {quantity} ({type(quantity)})"
        assert type(
            numpad) is bool, f"numpad should be a boolean, got {type(numpad)}"

        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = 1
        self.numpad = numpad
        # Check if its necesary to change the self.quantity value
        if not quantity == 1:
            self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def has_numpad(self):
        if self.numpad is True:
            print(f"The {self.name} has a numpad")
        else:
            print(f"The {self.name} dosen't has a numpad")


item1 = Item("Phone", 100, 5, False)
item2 = Item("Laptop", 1000, 3, True)

"""The time complexity of the code you provided is O(1), 
or constant time. This is because the operations being
performed in the __init__ method and calculate_total_price
method are simple assignments and arithmetic operations,
which take a constant amount of time regardless of the size of the inputs.
"""
