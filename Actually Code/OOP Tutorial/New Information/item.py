import csv


class Item:
    all = []
    PAY_RATE = 0.8

    def __init__(self, name: str, price: float = 0, quantity: int = 0):
        # Assign to self object

        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    def calculate_total_price(self):
        return self.__price * self.quantity

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

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.PAY_RATE

    def apply_increment(self, increment_value):
        self.__price = self.__price + increment_value

    @property
    def name(self):
        print("You are trying to get name")
        return self.__name

    @name.setter
    def name(self, value):
        print("You are trying to change the name")
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

    def __connect(self, smpt_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone.
        Wne have {self.name} {self.quantity} time.
        Regards, have a good night
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()

