from item import Item

item1 = Item("MyItem", 750)
item1.apply_discount()
item1.apply_increment(0.2)
print(item1)
print(item1.is_integer(item1.price))