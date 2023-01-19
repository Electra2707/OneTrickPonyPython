class Item:
    all = []
    def __init__(self, name: str, price: float or int, quantity: int):
        # Run validations to the recived arguments
        assert type(name) is str, f"name should be a string, got {type(name)}"
        assert price >= 0 and (type(price) is float or type(
            price) is int), f"price should be a float/int greater or equal than 0, got {price} ({type(price)})"
        assert quantity >= 0 and type(
            quantity) is int, f"quantity should be an integer greater or equal than 0, got {quantity} ({type(quantity)})"
        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = 1
        if not quantity == 1:  # Check if its necesary to change the self.quantity value
            self.quantity = quantity
        # Actions to execute
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Calbe", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyborad", 75, 5)

print(Item.all)

# for instance in Item.all:
#     print(instance.name)
