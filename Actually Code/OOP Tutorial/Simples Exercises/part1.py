"""Create a Person class that has a name and age attribute,
and a method called introduce() that prints "Hi, my name is
[name] and I am [age] years old."
"""


class Person:
    """The Class Person will ask for an input of a name and a age
    then it will generate 2 functions, the __init__ and the introduce
    """
    def __init__(self, name: str, age: int):
        """Create a attributes of the code

        :param name: The user_name
        :type name: str
        :param age: The user_age
        :type age: int
        """
        assert isinstance(name) is str, f"The input {name}, isn't a string"
        assert isinstance(age) is int, f"The input {age}, isn't a integral number"
        self.name = name
        self.age = age

    def introduce(self):
        """This functions takes the self.name and the self.age and
        it will print a introductory message
        """
        print(f"Hi, my name is {self.name}, and I am {self.age} years old")


person1 = Person("Pepe", 25)
person1.introduce()
person2 = Person("Maria", 15)
person2.introduce()
